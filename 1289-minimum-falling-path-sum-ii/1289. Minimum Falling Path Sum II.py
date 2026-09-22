class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid)

        dp = [[float('inf')] * cols for _ in range(rows + 1)] # dp[r][c] = # ways to get to row r, with prev col selection of c on row (r-1)

        for c in range(cols):
            dp[0][c] = 0
        
        for r in range(1, rows+1):
            for c in range(cols):
                for nxt_c in range(cols):
                    if c == nxt_c and cols != 1:
                        continue 
                    if dp[r-1][c] != float('inf'):
                        dp[r][nxt_c] = min(dp[r][nxt_c], dp[r-1][c] + grid[r-1][nxt_c])
        return min(dp[-1])
        # @cache
        # def dfs(row_level, prev_selected_col):
        #     if row_level == rows:
        #         return 0
            
        #     res = float('inf')
        #     for c in range(cols):
        #         if c != prev_selected_col:
        #             res = min(res, grid[row_level][c] + dfs(row_level + 1, c))
            
        #     return res
        
        # return dfs(0, -1)