class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            if grid[r][0] == 0: #flip entire row
                for c in range(cols):
                    grid[r][c] ^= 1
        for c in range(cols):
            ones = 0
            for r in range(rows):
                if grid[r][c] == 1:
                    ones += 1
            if ones <= rows // 2: #flip all cols
                for r in range(rows):
                    grid[r][c] ^= 1
        
        res = 0
        print(grid)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: 
                    res += 2 ** (cols - c - 1)

        return res