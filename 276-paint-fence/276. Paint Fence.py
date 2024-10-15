class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1: return k
        if n == 2: return k*k

        dp = [0] * (n)
        dp[0]=k
        dp[1]=k*k
        for i in range(2, n):
            dp[i] = (k-1) * dp[i-1] + (k-1) * dp[i-2]
        return dp[-1]
