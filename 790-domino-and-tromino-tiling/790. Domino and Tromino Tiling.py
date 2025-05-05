class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        @cache
        def dp(n):
            if n < 0:
                return 0
            if n == 1 or n == 0:
                return 1
            if n == 2:
                return 2
            res = 0
            for i in range(1, n + 1):
                if i == 1 or i == 2:
                    res += dp(n-i)
                else:
                    res += 2*dp(n-i)
            return res % MOD             
            # return dp(n-1) + dp(n-2) + 2*dp(n-3) + 2*dp(n-4) + 2*dp(n-5)
        return dp(n)