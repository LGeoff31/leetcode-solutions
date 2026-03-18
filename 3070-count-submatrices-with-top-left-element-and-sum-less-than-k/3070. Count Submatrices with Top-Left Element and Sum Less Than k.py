class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[0] * cols for _ in range(rows)]
        dp[0][0] = grid[0][0]

        # fill first row
        for c in range(1, cols):
            dp[0][c] = grid[0][c] + dp[0][c-1]
        # fill first col
        for r in range(1, rows):
            dp[r][0] = grid[r][0] + dp[r-1][0]
        
        for r in range(1, rows):
            for c in range(1, cols):
                dp[r][c] = dp[r-1][c] + dp[r][c-1] - dp[r-1][c-1] + grid[r][c]
        return sum(dp[r][c] <= k for r in range(rows) for c in range(cols))