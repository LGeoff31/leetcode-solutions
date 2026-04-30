class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        @cache
        def dfs(r,c, cost):
            if not (0 <= r < rows and 0 <= c < cols) or cost < 0:
                return -float('inf')
            if r == rows - 1 and c == cols - 1:
                if grid[r][c] == 0:
                    return 0
                elif grid[r][c] == 1:
                    return 1 if cost >= 1 else -float('inf')
                else:
                    return 2 if cost >= 1 else -float('inf')

            res = -float('inf')
            # GO RIGHT
            if grid[r][c] == 0:
                res = max(res, dfs(r, c+1, cost))
                res = max(res, dfs(r+1, c, cost))
            elif grid[r][c] == 1:
                res = max(res, 1 + dfs(r,c+1, cost-1))
                res = max(res, 1 + dfs(r+1, c, cost-1))
            else:
                res = max(res, 2 + dfs(r, c+1, cost-1))
                res = max(res, 2 + dfs(r+1, c, cost-1))
            return res
        res = dfs(0, 0, k)
        dfs.cache_clear()
        if res != -float('inf'):
            return res
        return -1

