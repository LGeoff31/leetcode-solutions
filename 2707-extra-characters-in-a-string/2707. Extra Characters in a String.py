class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        lookup = set(dictionary)
        @cache
        def dfs(idx):
            if idx == len(s): return 0

             #skipping character
            res = 1 + dfs(idx+1)
            #no skipping character
            for i in range(idx, len(s)):
                if s[idx:i+1] in lookup: 
                    res = min(res,dfs(i+1))
            return res
        return dfs(0)


        