class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1: return k
        if n == 2: return k*k

        dp = [0] * (n)
        dp[0]=k
        dp[1]=k*k
        prevprev, prev = k, k*k
        for i in range(2, n):
            dp[i] = (k-1) * prev + (k-1) * prevprev
            prevprev = prev
            prev = dp[i]
        return dp[-1]
