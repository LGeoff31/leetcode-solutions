class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1: return triangle[0][0]
        # dp = [[0], [0,0], [0,0,0], [0,0,0,0]]
        dp = []
        for i in range(len(triangle)):
            a = []
            for j in range(i+1):
                a.append(0)
            dp.append(a)
        #dp[i][j] = minSum if you go on the square triangle[i][j]
        dp[0][0] = triangle[0][0]
        dp[1][0] = triangle[1][0] + dp[0][0]
        dp[1][1] = triangle[1][1] + dp[0][0]
        print(dp)
        for i in range(2, len(triangle)): #2 -> 3
            for j in range(i+1): #0 -> 2
                if j == 0:
                    dp[i][j] = triangle[i][j] + dp[i-1][j]
                elif j == i:
                    dp[i][j] = triangle[i][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = min(triangle[i][j] + dp[i-1][j-1], triangle[i][j] + dp[i-1][j])
        res = 1e9
        for num in dp[-1]:
            res = min(res, num)
        return res
        