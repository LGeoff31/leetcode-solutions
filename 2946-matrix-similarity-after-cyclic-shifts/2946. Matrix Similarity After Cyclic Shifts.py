class Solution:
    def areSimilar(self, grid: List[List[int]], k: int) -> bool:
        org_grid = copy.deepcopy(grid)
        rows, cols = len(grid), len(grid[0])
        for i in range(k):
            for r in range(rows):
                row_copy = grid[r].copy()
                if r % 2 == 0:
                    row_copy = [row_copy[-1]] + row_copy[:-1]
                else:
                    row_copy = row_copy[1:] + [row_copy[0]]
                grid[r] = row_copy
            print(grid)
        return grid == org_grid
