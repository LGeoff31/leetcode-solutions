class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows, cols = [0] * m, [0] * n


        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    rows[r] += 1
                    cols[c] += 1
        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    if rows[r] > 1 or cols[c] > 1:
                        res += 1
        return res


