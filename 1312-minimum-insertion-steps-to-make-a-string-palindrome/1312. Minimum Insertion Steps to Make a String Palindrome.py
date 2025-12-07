class Solution:
    def minInsertions(self, s: str) -> int:
        @cache
        def dfs(l, r):
            if l >= r:
                return 0
            
            res = 1e9
            if s[l] == s[r]:
                res = min(res, dfs(l+1, r-1))
            else:
                res = min(res, 1+dfs(l+1, r), 1+dfs(l,r-1))
            return res
        return dfs(0, len(s) - 1)