class Solution:
    def maximumAmount(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        @cache
        def dfs(r,c,uses):
            if r == rows - 1 and c == cols - 1: 
                if uses < 2:
                    return max(grid[r][c], 0) 
                else:
                    return grid[r][c]
            if not (0 <= r < rows and 0 <= c < cols):
                return -1e9
    
            if uses < 2:
                return max(grid[r][c] + max(dfs(r+1, c, uses), dfs(r, c+1, uses)), max(dfs(r+1, c, uses+1), dfs(r, c+1, uses+1)))
            else:
                return grid[r][c] + max(dfs(r+1, c, uses), dfs(r, c+1, uses))
        return dfs(0, 0, 0) 
        