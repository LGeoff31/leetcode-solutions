class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        lookup = set(wordDict)
        @cache
        def dfs(idx):
            if idx == len(s): return True

            for i in range(idx, len(s)):
                if s[idx: i+1] in lookup:
                    if dfs(i+1): return True 
            return False
        return dfs(0)

