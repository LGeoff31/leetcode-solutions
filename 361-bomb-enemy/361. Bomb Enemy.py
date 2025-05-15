class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        res = 0
        row_hits = 0
        col_hits = [0] * cols

        for r in range(rows):
            for c in range(cols):
                # Recompute row_hits only if we're at the start or after a wall
                if c == 0 or grid[r][c - 1] == 'W':
                    row_hits = 0
                    k = c
                    while k < cols and grid[r][k] != 'W':
                        if grid[r][k] == 'E':
                            row_hits += 1
                        k += 1

                # Recompute col_hits[c] only if we're at the start or after a wall
                if r == 0 or grid[r - 1][c] == 'W':
                    col_hits[c] = 0
                    k = r
                    while k < rows and grid[k][c] != 'W':
                        if grid[k][c] == 'E':
                            col_hits[c] += 1
                        k += 1

                if grid[r][c] == '0':
                    res = max(res, row_hits + col_hits[c])

        return res
