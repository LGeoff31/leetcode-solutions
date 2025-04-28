class Solution:
    def distinctSequences(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        # 1001
        @cache
        def dfs(rolls, prevVal, prevPrevVal):
            if rolls == n:
                return 1
            res = 0
            for i in range(1, 7):
                if gcd(i, prevVal) == 1 and i != prevPrevVal and i != prevVal:
                    res += dfs(rolls + 1, i, prevVal)
            return res % MOD

        return dfs(0, -1, -1) % MOD