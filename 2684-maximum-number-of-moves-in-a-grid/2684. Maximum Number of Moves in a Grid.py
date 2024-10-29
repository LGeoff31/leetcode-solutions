class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        res = 0
        for j in range(1, n):
            for i in range(m):
                if i > 0 and grid[i - 1][j - 1] < grid[i][j] and dp[i - 1][j - 1]:
                    res = max(res, j)
                    dp[i][j] = j
                    continue
                if grid[i][j - 1] < grid[i][j] and dp[i][j - 1]:
                    res = max(res, j)
                    dp[i][j] = j
                    continue
                if i < m - 1 and grid[i + 1][j - 1] < grid[i][j] and dp[i + 1][j - 1]:
                    res = max(res, j)
                    dp[i][j] = j
                    continue
        return res
            
        