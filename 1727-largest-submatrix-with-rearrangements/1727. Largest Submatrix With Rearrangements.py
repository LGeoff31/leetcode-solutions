class Solution:
    def largestSubmatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        columns = [[0] * cols for _ in range(rows)]
        for c in range(cols):
            curr = int(grid[0][c] == 1)
            columns[0][c] = curr
            for r in range(1, rows):
                if grid[r][c] == 1:
                    curr += 1
                else:
                    curr = 0
                columns[r][c] = curr
        rows_prefix = []
        print(columns)
        for r in range(rows):
            col_values = []
            for c in range(cols):
                col_values.append(columns[r][c])
            col_values.sort()
            rows_prefix.append(col_values)
        res = 0
        for r in range(len(rows_prefix)):
            row = rows_prefix[r]
            print('row', row)
            for c in range(len(row)):
                res = max(res, row[c] * (len(row) - c))


        return res