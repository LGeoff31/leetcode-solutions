class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[1e9] * n for _ in range(n)]

        #fill in first row
        for c in range(n):
            dp[0][c] = grid[0][c]
        

        for r in range(1, n):
            for c in range(n):
                for new_c in range(n):
                    if c != new_c: dp[r][c] = min(dp[r][c], dp[r-1][new_c] + grid[r][c])
        return min(dp[-1])
        