class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def square(r,c):
            CONSTANT_SUM = grid[r][c] + grid[r][c+1] + grid[r][c+2]
            unique = set()
            for dr in range(3):
                row_sum = 0
                for dc in range(3):
                    # ROW
                    row_sum += grid[r+dr][c+dc]
                    unique.add(grid[r+dr][c+dc])
                if row_sum != CONSTANT_SUM: return False
            
            for dc in range(3):
                col_sum = 0
                for dr in range(3):
                    # ROW
                    col_sum += grid[r+dr][c+dc]
                if col_sum != CONSTANT_SUM: return False

            # DIAGONALS
            return grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] == grid[r+2][c] + grid[r+1][c+1] + grid[r][c+2] == CONSTANT_SUM and len(unique) == 9 and max(unique) == 9
        res = 0
        for r in range(rows - 2):
            for c in range(cols - 2):
                res += square(r,c)
        return res
