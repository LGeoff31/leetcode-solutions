class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        res = 0
        MOD = 10 ** 9 + 7
        rows, cols = len(grid), len(grid[0])
        # NOTE: USE For _ in range(20) instead of * 20 because i think that leads to some copying memory issues
        dp = [[[-1] * 20 for _ in range(cols)] for _ in range(rows)]  
        def dfs(r, c, curr):
            if r >= rows or c >= cols:
                return 0

            curr ^= grid[r][c]
            if dp[r][c][curr] != -1:
                return dp[r][c][curr]
            # print(r,c,curr,'reached')
            if r == rows - 1 and c == cols - 1:
                return curr == k
            right = dfs(r, c+1, curr)
            down = dfs(r+1, c, curr)
            dp[r][c][curr] = (right + down) % MOD
            return dp[r][c][curr]
        ans = dfs(0, 0, 0)
        # print(dp)
        return ans % MOD