class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[1e9] * cols for _ in range(rows)]
        # Base case
        dp[0][0] = grid[0][0]
        for c in range(1, cols):
            dp[0][c] = dp[0][c-1] + grid[0][c]
        for r in range(1, rows):
            dp[r][0] = dp[r-1][0] + grid[r][0]
        print(dp)
        for r in range(1, rows):
            for c in range(1, cols):
                dp[r][c] = min(dp[r-1][c], dp[r][c-1]) + grid[r][c]
        return dp[-1][-1]

