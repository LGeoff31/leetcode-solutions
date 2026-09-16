class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        """
        x1 + x2 + x3 + ... + xk <= n, where xi >= 1
        """
        MOD = 10 ** 9 + 7

        dp = [1] * n

        for _ in range(k):
            new_dp = [0] * n
            f = 0
            for i in range(1, len(dp)):
                f += dp[i-1]
                new_dp[i] += new_dp[i-1] + f
            dp = new_dp
        return dp[n-1] % MOD