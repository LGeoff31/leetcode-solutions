class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows, cols = len(dungeon), len(dungeon[0])
        if rows == 1 and cols == 1:
            if dungeon[0][0] >= 0: return 1
            else: return 1 - dungeon[0][0]
        dp = [[1e9] * cols for _ in range(rows)]
        #bottom up
        dp[rows-1][cols-1] = dungeon[rows-1][cols-1]
        #fill in bottom row
        for c in range(cols-2, -1, -1):
            dp[rows-1][c] = min(0,min(dungeon[rows-1][c], 0, dungeon[rows-1][c] + dp[rows-1][c+1]))
        #fill in last column
        for r in range(rows-2, -1, -1):
            dp[r][cols-1] = min(0, min(dungeon[r][cols-1], 0, dungeon[r][cols-1] + dp[r+1][cols-1]))

        for r in range(rows-2, -1, -1):
            for c in range(cols-2, -1, -1):
                dp[r][c] = min(0,dungeon[r][c] + max(dp[r+1][c], dp[r][c+1]))
        print(dp)
        if dp[0][0] > 1: return 1
        return 1 + abs(dp[0][0])



            

