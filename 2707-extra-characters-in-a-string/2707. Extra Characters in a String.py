class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        lookup = set(dictionary)
        memo = {}
        def dfs(idx):
            if idx == len(s): return 0
            if idx in memo:
                return memo[idx]
             #skipping character
            res = 1 + dfs(idx+1)
            #no skipping character
            for i in range(idx, len(s)):
                if s[idx:i+1] in lookup: 
                    res = min(res,dfs(i+1))
            memo[idx] = res
            return res
        return dfs(0)


        