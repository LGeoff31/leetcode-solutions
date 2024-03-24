class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        lookup = set(wordDict)
        memo = {}
        def dfs(idx):
            if idx == len(s): return True
            if idx in memo:
                return memo[idx]
            for i in range(idx, len(s)):
                if s[idx: i+1] in lookup:
                    memo[i+1] = dfs(i+1)
                    if memo[i+1]: return True 
            return False
        return dfs(0)

