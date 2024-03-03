class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        if n == 3: return 5
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        dp[2] = 5
        for i in range(3, n):
            dp[i] = 2*dp[i-1] + dp[i-3]
        return dp[-1] % (10**9 + 7)




        