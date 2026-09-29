class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        @cache
        def dfs(r,c, net_in):
            if not (0 <= r < rows and 0 <= c < cols):
                return False
            
            new_net_in = net_in + (1 if grid[r][c] == "(" else -1)
            if new_net_in < 0:
                return False

            if r == rows - 1 and c == cols - 1:
                return new_net_in == 0

            return dfs(r+1, c, new_net_in) or dfs(r, c+1, new_net_in)
        return dfs(0, 0, 0)