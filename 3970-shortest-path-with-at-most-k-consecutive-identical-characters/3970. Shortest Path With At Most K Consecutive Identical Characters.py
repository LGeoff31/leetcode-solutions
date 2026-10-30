class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj = defaultdict(list)

        for u, v, w in edges:
            adj[u].append((v, w))

        best = [k+1] * n
        heap = [(0, 1, 0)] # (distance, run, node)

        while heap:
            d, run, x = heappop(heap)
            if run >= best[x]:
                continue 
            if x == n-1:
                return d
            
            best[x] = run
            for y, w in adj[x]:
                r = run + 1 if labels[y] == labels[x] else 1
                if r < best[y]:
                    heappush(heap, (d + w, r, y))
        return -1