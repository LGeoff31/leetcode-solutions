class Solution:
    def cyclicShift(self, n: int, grid: list[list[int]], rowShift: list[int], colShift: list[int]) -> list[list[int]]:
        def shift_row(idx, val):
            nonlocal grid
            val %= len(grid[idx])
            grid[idx] = grid[idx][val:] + grid[idx][:val] if val else grid[idx]

        def shift_col(idx, val):
            nonlocal grid 
            val %= len(grid)
            col_vals = [grid[r][idx] for r in range(len(grid))]
            col_vals = col_vals[val:] + col_vals[:val] if val else col_vals

            for r in range(len(grid)):
                grid[r][idx] = col_vals[r]

        for idx, val in enumerate(rowShift):
            shift_row(idx, val)
        
        for idx, val in enumerate(colShift):
            shift_col(idx, val)
        return grid