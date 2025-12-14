class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10 ** 9 + 7
        @cache
        def dfs(idx, cnt):
            if idx == len(corridor):
                return cnt == 2
            if cnt >= 3:
                return 0
            res = 0
            if cnt == 2:
                res += dfs(idx + 1, 0 + int(corridor[idx] == "S"))
            res += dfs(idx + 1, cnt + int(corridor[idx] == "S"))
            return res % MOD
        res = dfs(0, 0) % MOD
        dfs.cache_clear()
        return res
