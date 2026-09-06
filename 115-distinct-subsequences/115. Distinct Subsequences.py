class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @cache
        def dfs(i, currString): #O(N * 2^N)
            if currString == t:
                return 1
            
            if i >= len(s):
                return 0

            res = dfs(i+1, currString)
            if len(currString) < len(t) and t[len(currString)] == s[i]:
                res += dfs(i+1, currString + s[i]) 
            
            return res
        return dfs(0, "")