class neighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

    def adjacentSum(self, value: int) -> int:
        rows = self.rows
        cols = self.cols
        a,b = -1, -1
        for r in range(rows):
            for c in range(cols):
                if self.grid[r][c] == value:
                    a,b = r,c
        z = [(-1,0), (1,0), (0,-1), (0,1)]
        res = 0
        for x,y in z:
            if 0 <= a+x < rows and 0 <= b+y < cols:
                res += self.grid[a+x][b+y]

        return res

    def diagonalSum(self, value: int) -> int:
        rows = self.rows
        cols = self.cols
        a,b = -1, -1
        for r in range(rows):
            for c in range(cols):
                if self.grid[r][c] == value:
                    a,b = r,c
        z = [(-1,-1), (1,1), (1,-1), (-1,1)]
        res = 0
        for x,y in z:
            if 0 <= a+x < rows and 0 <= b+y < cols:
                res += self.grid[a+x][b+y]

        return res

        


# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)