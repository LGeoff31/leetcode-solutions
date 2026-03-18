class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        # dp[i][j] = sum of elements to j in row i
        dp = [[0] * (len(grid[0]) + 1) for _ in range(len(grid) + 1)]
        submatrices = 0
        # best way to find sum of matrix ending at (i, j):
        # dp[i - 1]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                dp[i + 1][j + 1] = dp[i][j + 1] + dp[i + 1][j] - dp[i][j] + grid[i][j]
                if dp[i + 1][j + 1] <= k:
                    submatrices += 1
                # dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

        return submatrices