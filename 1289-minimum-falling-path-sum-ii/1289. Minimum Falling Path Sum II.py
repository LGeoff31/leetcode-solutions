class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid)
        @cache
        def dfs(row_level, prev_selected_col):
            if row_level == rows:
                return 0
            
            res = float('inf')
            for c in range(cols):
                if c != prev_selected_col:
                    res = min(res, grid[row_level][c] + dfs(row_level + 1, c))
            
            return res
        
        return dfs(0, -1)