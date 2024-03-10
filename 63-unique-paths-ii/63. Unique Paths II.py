class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        dp = [[0] * len(grid[0]) for _ in range(len(grid))]
        dp[0][0] = 1
        if grid[0][0] == 1: return 0
        if len(grid) == 1 and len(grid[0]) == 1: 
            return 1 if grid[0][0] == 0 else 0

        #fill in the row and break whenver coming across obstacle   
        for c in range(1, len(grid[0])):
            if grid[0][c] != 1:
                dp[0][c] = 1
            else: 
                break
        
        #fill in the first column
        for r in range(1, len(grid)):
            if grid[r][0] != 1:
                dp[r][0] = 1
            else:
                break
        
        for r in range(1, len(grid)):
            for c in range(1, len(grid[0])):
                if grid[r][c] != 1:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
        return dp[-1][-1]

        