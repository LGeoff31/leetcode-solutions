class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        minHeap = [(grid[0][0], 0, 0)]
        visited = set((0,0))
        def in_bounds(r,c):
            return min(r,c) >= 0 and max(r,c) < n
        while minHeap:
            min_dist, r, c = heapq.heappop(minHeap)
            if (r,c) == (n-1, n-1):
                return min_dist
            nei = [(r+1, c), (r-1, c), (r,c+1), (r,c-1)]
            for r2, c2 in nei:
                if in_bounds(r2,c2) and (r2,c2) not in visited:
                    visited.add((r2,c2))
                    heapq.heappush(minHeap, (max(min_dist, grid[r2][c2]), r2, c2))



        