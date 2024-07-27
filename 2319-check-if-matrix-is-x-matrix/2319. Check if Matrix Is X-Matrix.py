class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        for i in range(n):
            if grid[i][i] == 0: return False
            if grid[n-i-1][n-i-1] == 0: return False
        zero = 0
        for r in range(n):
            for c in range(n):
                zero += grid[r][c] == 0
        return n*n - 2*n == zero if n%2==0 else n*n-2*(n-1)-1 == zero
        