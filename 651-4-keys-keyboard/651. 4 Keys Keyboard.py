class Solution:
    def maxA(self, n: int) -> int:
        dp = [0] * (n+1)
        for i in range(1, n+1):
            dp[i] = dp[i-1] + 1
            for j in range(i - 2): # Try to copy paste
                dp[i] = max(dp[i], dp[j] * (i - j - 1))
        return dp[-1]