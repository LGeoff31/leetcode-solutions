class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)

        def dfs(idx):
            if idx == len(s):
                res.append(" ".join(curr))

            for i in range(idx, len(s)):
                substring = s[idx:i+1]
                if substring in words:
                    curr.append(substring)
                    dfs(i+1)
                    curr.pop()

        curr = []
        res = []
        dfs(0)
        return res
        