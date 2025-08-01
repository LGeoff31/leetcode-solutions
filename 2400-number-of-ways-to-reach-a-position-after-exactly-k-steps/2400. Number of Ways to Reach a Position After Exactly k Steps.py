class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        @cache
        def dfs(position, k):
            if k == 0:
                return position == endPos
            
            return dfs(position+1, k-1) + dfs(position-1, k-1)
        return dfs(startPos, k) % MOD