class Solution:
    def minimumEffortPath(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dist = [[1e9 for _ in range(cols)] for _ in range(rows)]
        dist[0][0] = 0
        minHeap = [(0,0,0)]

        def in_bounds(r,c):
            return 0 <= r < rows and 0 <= c < cols
        while minHeap:
            effort, r,c = heapq.heappop(minHeap)
            if (r,c) == (rows-1, cols-1):
                return effort

            nei = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
            for r2, c2 in nei:
                if in_bounds(r2, c2):
                    new_effort = max(effort, abs(grid[r][c] - grid[r2][c2]))
                    if new_effort < dist[r2][c2]:
                        dist[r2][c2] = new_effort
                        heapq.heappush(minHeap, (new_effort, r2, c2))