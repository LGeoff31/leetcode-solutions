class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        operations = 0
        
        for col in range(n):
            for row in range(m - 1):
                if grid[row][col] >= grid[row + 1][col]:
                    increment = grid[row][col] - grid[row + 1][col] + 1
                    grid[row + 1][col] += increment
                    operations += increment
        
        return operations