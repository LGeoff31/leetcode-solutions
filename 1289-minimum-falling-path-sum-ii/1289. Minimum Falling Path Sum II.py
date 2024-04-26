class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        for i in range(1,n):
            ans=heapq.nsmallest(2,grid[i-1])
            for j in range(m):
                if grid[i-1][j]==ans[0]:
                    grid[i][j]+=ans[1]
                else:
                    grid[i][j]+=ans[0]
        return min(grid[-1])                