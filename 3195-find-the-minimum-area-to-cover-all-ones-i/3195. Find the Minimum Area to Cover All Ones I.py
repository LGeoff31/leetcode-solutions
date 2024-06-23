class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        row, col = [], []
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    row.append(r)
                    col.append(c)
        print(row, col)
        row.sort()
        col.sort()
        return (row[-1] - row[0] + 1) * (col[-1] - col[0] + 1)