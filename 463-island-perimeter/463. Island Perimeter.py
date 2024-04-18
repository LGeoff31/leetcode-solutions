class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        if grid[0][0] == 1: res+=4
        rows, cols = len(grid), len(grid[0])
        #first row
        for c in range(1, cols):
            if grid[0][c] == 1:
                if grid[0][c-1] == 1:
                    res+=2
                else:
                    res+=4
        #first col
        for r in range(1, rows):
            if grid[r][0] == 1:
                if grid[r-1][0] == 1:
                    res+=2
                else:
                    res += 4
        print(res)
        #secoudn row down
        for r in range(1, rows):
            for c in range(1, cols):
                if grid[r][c] == 1:
                    res+=4
                    if grid[r-1][c] == 1: res -= 2
                    if grid[r][c-1] == 1: res -= 2
        return res
                


        