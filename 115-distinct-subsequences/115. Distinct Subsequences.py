class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @cache
        def dfs(i, j): #O(N * N)
            if j == len(t):
                return 1
            
            if i >= len(s):
                return 0

            res = dfs(i+1, j)
            if j < len(t) and t[j] == s[i]:
                res += dfs(i+1, j+1) 
            
            return res
        return dfs(0, 0)