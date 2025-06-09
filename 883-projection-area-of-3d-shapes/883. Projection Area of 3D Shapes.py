class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        zeros = 0
        for r in range(rows):
            for c in range(cols):
                zeros += grid[r][c] == 0
        # sum of rows * cols
        # sum(grid[-1])
        # Sum(g)
        max_each_row = []
        max_each_col = []

        for r in range(rows):
            a = -1e9
            for c in range(cols):
                a = max(a, grid[r][c])
            max_each_row.append(a)
        for c in range(rows):
            a = -1e9
            for r in range(cols):
                a = max(a, grid[r][c])
            max_each_col.append(a)
        print(max_each_row)
        print(max_each_col)

        return rows * cols - zeros + sum(max_each_row) + sum(max_each_col)
        # res = rows * cols
        # res += sum(arr[-1] for arr in grid)
        # res += sum(grid[-1])
        # return res