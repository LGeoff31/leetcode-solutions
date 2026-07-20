class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        for _ in range(k):
            copy_grid = deepcopy(grid)
            for r in range(rows):
                for c in range(cols):
                    if c == cols - 1 and r < rows - 1:
                        copy_grid[r+1][0] = grid[r][cols-1]
                    elif r == rows - 1 and c == cols - 1:
                        copy_grid[0][0] = grid[rows-1][cols-1]
                    elif c < cols - 1:
                        copy_grid[r][c+1] = grid[r][c]
            grid = copy_grid
        return grid
