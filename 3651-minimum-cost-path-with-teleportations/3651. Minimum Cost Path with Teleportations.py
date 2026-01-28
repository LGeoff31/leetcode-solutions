from typing import List
import heapq
from bisect import bisect_right

INF = 10**18

class DSUNext:
    # "disjoint set of next pointers" for skipping processed indices
    def __init__(self, n: int):
        self.parent = list(range(n + 1))  # n is sentinel "end"

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def erase(self, x: int) -> None:
        # mark x as processed: next(x) becomes find(x+1)
        self.parent[x] = self.find(x + 1)


class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        n = rows * cols

        def idx(r: int, c: int) -> int:
            return r * cols + c

        # cells sorted by value (ascending)
        cells = []
        for r in range(rows):
            for c in range(cols):
                cells.append((grid[r][c], idx(r, c)))
        cells.sort()
        values = [v for v, _ in cells]

        # dist[t][i] : min cost to reach cell i using exactly t teleports
        dist = [[INF] * n for _ in range(k + 1)]
        dist[0][0] = 0

        pq = [(0, 0, 0)]  # (d, t, i)

        # For each layer L (0..k), we maintain a DSU of indices in `cells`
        # that have NOT yet been teleport-relaxed INTO layer L.
        #
        # When we pop a node at layer (L-1), we may teleport into layer L.
        # So we need DSU for layers 1..k. (Layer 0 has no incoming teleports.)
        teleport_dsu = [None] + [DSUNext(n) for _ in range(k)]

        target = idx(rows - 1, cols - 1)

        while pq:
            d, t, i = heapq.heappop(pq)
            if d != dist[t][i]:
                continue

            if i == target:
                # This is optimal for this (t, target). We still might do better with fewer teleports
                # but since pq pops globally, this is the best across all states popped so far.
                # We'll still just finish via min at the end, or early-exit if you want:
                pass

            r, c = divmod(i, cols)

            # Normal moves (same teleport count)
            if r + 1 < rows:
                j = idx(r + 1, c)
                nd = d + grid[r + 1][c]
                if nd < dist[t][j]:
                    dist[t][j] = nd
                    heapq.heappush(pq, (nd, t, j))

            if c + 1 < cols:
                j = idx(r, c + 1)
                nd = d + grid[r][c + 1]
                if nd < dist[t][j]:
                    dist[t][j] = nd
                    heapq.heappush(pq, (nd, t, j))

            # Teleport to layer t+1 (cost 0), to any cell with value <= current value
            if t < k:
                v = grid[r][c]
                upto = bisect_right(values, v)  # indices [0, upto) are eligible
                dsu = teleport_dsu[t + 1]
                p = dsu.find(0)
                while p < upto:
                    _, cell_id = cells[p]
                    if d < dist[t + 1][cell_id]:
                        dist[t + 1][cell_id] = d
                        heapq.heappush(pq, (d, t + 1, cell_id))
                    dsu.erase(p)
                    p = dsu.find(p)

        return min(dist[t][target] for t in range(k + 1))
