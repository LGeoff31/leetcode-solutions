class Solution:
    def trapRainWater(self, grid: List[List[int]]) -> int:
        minHeap = []
        rows, cols = len(grid), len(grid[0])
        if rows < 3 or cols < 3: return 0
        if not grid or not grid[0]: return 0

        for r in range(rows):
            for c in range(cols):
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    heappush(minHeap, (grid[r][c], r, c))
                    grid[r][c] = -1
        
        level = 0
        res = 0

        while minHeap:
            height, r,c = heappop(minHeap)
            level = max(level, height)

            for new_r, new_c in [(r-1, c), (r+1, c), (r, c+1), (r, c-1)]:
                if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] != -1:
                    heappush(minHeap, (grid[new_r][new_c], new_r, new_c))
                    if grid[new_r][new_c] < level:
                        res += level - grid[new_r][new_c]
                    grid[new_r][new_c] = -1
        return res