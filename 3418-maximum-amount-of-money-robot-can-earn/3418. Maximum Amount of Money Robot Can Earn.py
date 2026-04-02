class Solution:
    def maximumAmount(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        @cache
        def dfs(r,c,robbers):
            if r == rows - 1 and c == cols - 1:
                if robbers > 0:
                    return max(0, grid[r][c])
                return grid[r][c]
            if not (0 <= r < rows and 0 <= c < cols):
                return -1e9
            res = -1e9
            # DOWN PATH
            res = max(res, dfs(r+1, c, robbers) + grid[r][c])
            if robbers > 0:
                res = max(res, dfs(r+1, c, robbers - 1))
            
            # RIGHT PATH
            res = max(res, dfs(r, c+1, robbers) + grid[r][c])
            if robbers > 0:
                res = max(res, dfs(r, c+1, robbers - 1))
            return res
        res = dfs(0, 0, 2)
        dfs.cache_clear()
        return res