class Solution:
    def coloredCells(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        if n == 1: return 1
        dp[1] = 5
        width = 3
        for i in range(2, n):
            dp[i] = dp[i-1] + 4*width-4
            width += 1
        # print(dp)
        return dp[-1]


        