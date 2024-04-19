class Solution:
    def updateMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        mx = rows * cols
        dp = [[mx] * cols for _ in range(rows)]

        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                if grid[r][c] == 0: dp[r][c] = 0
                else: 
                    right = dp[r][c+1] if c+1 < cols else mx
                    down = dp[r+1][c] if r+1 < rows else mx
                    dp[r][c] = 1 + min(right, down)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    dp[r][c] = 0
                else:
                    top = dp[r-1][c] if r-1 >= 0 else mx
                    left = dp[r][c-1] if c-1>=0 else mx
                    dp[r][c] = min(dp[r][c], 1 + min(top, left))
        return dp