class Solution:
    def areSimilar(self, grid: List[List[int]], k: int) -> bool:
        rows, cols = len(grid), len(grid[0])
        k%=cols
        for row in grid:
            if row != row[k:] + row[0:k]: return False
        return True
        