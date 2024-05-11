class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if r+1 < rows and grid[r+1][c] != grid[r][c]:
                    return False
                if c+1 < cols and grid[r][c] == grid[r][c+1]:
                    return False
        return True
        