class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        board = [[1] * n for _ in range(n)]
        def dfs(r, grid):
            for c in range(n):
                if r == n-1 and grid[r][c]:
                    self.res+=1
                elif grid[r][c]:
                    a = copy.deepcopy(grid)
                    #remove all beneath
                    new_r = r+1
                    while new_r < n:
                        a[new_r][c] = 0
                        new_r+=1
                    #remove all down right diagonal
                    new_r = r+1
                    new_c = c+1
                    while new_r < n and new_c < n:
                        a[new_r][new_c] = 0
                        new_r+=1
                        new_c+=1
                    #remove all down left diagonal
                    new_r = r+1
                    new_c = c - 1
                    while new_r < n and new_c >= 0:
                        a[new_r][new_c] = 0
                        new_r+=1
                        new_c-=1
                    dfs(r+1, a)
        
        dfs(0, board)
        return self.res