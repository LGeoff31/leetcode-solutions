class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        MOD = 10 ** 9 + 7
        @cache
        def dfs(r,c): # returns (most postive, most negative)
            if not (0 <= r < rows and 0 <= c < cols):
                return (-1e20, 1e20)
            if r == rows - 1 and c == cols - 1:
                return (grid[r][c], grid[r][c])
            
            possibility1 = dfs(r+1, c)
            possibility2 = dfs(r, c+1)

            if grid[r][c] < 0:
                most_positive = max(grid[r][c] * possibility1[1], grid[r][c] * possibility2[1]) 
                most_negative = min(grid[r][c] * possibility1[0], grid[r][c] * possibility2[0]) 
            else:
                most_positive = max(grid[r][c] * possibility1[0], grid[r][c] * possibility2[0]) 
                most_negative = min(grid[r][c] * possibility1[1], grid[r][c] * possibility2[1])

            return (most_positive, most_negative)
        res = int(dfs(0, 0)[0])
        print(res)
        return -1 if res < 0 else res % MOD