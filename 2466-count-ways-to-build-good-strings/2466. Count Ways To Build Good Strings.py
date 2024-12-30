class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10 ** 9 + 7
        @cache
        def dfs(size):
            if size > high:
                return 0
            if low <= size <= high:
                return 1 + dfs(size + zero) + dfs(size + one)
            res = 0

            res += dfs(size + zero)
            res += dfs(size + one)
            return res % MOD
        res = dfs(0)
        dfs.cache_clear()
        return res
            