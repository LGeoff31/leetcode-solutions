class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        """
        0 1 0
        0 0 1
        1 0 0

        0 1 1
        1 1 0
        """
        rows, cols = len(grid), len(grid[0])
        @cache
        def dfs(r,c):
            if r == rows - 1 and c == cols - 1:
                return 1
            
            if not (0 <= r < rows and 0 <= c < cols):
                return 0
            
            res = 0
            # Down

            right = True
            new_r, new_c = r+1, c
            while new_r < rows and new_c < cols and grid[new_r][new_c] == 1:
                if right:
                    new_c += 1
                else:
                    new_r += 1
                right = not right 

            res += dfs(new_r, new_c)

            # Right

            right = False
            new_r, new_c = r, c+1
            while new_r < rows and new_c < cols and grid[new_r][new_c] == 1:
                if right:
                    new_c += 1
                else:
                    new_r += 1
                right = not right 
            res += dfs(new_r, new_c)
            return res
        return dfs(0, 0) % (10 ** 9 + 7)