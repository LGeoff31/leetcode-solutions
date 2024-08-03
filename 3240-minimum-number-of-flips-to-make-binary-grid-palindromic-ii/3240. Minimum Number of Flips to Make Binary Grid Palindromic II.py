class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:   
        rows, cols = len(grid), len(grid[0])
        res = 0
        single = 0 #(1,0)
        double = 0 #(1,1)

        for r in range(rows//2):
            for c in range(cols//2):
                ones = grid[r][c] + grid[r][cols - c - 1] + grid[rows - r - 1][c] + grid[rows-r-1][cols-c-1]
                res += min(ones, 4-ones)

            # Middle column
            if cols % 2 == 1:
                ones = grid[r][cols//2] + grid[rows - r - 1][cols//2]
                single += ones == 1
                double += ones == 2
        # Middle row
        if rows % 2 == 1:
            for c in range(cols // 2):
                ones = grid[rows//2][c] + grid[rows//2][cols-c-1]
                single += ones == 1
                double += ones == 2
            if cols % 2 == 1:
                res += grid[rows//2][cols//2]
        if double % 2 == 0 or single > 0:
            return res + single
        return res + 2