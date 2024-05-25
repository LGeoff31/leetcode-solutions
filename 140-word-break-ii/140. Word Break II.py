class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)

        @cache
        def dfs(idx):
            if idx == len(s):
                return [""]

            res = []
            for i in range(idx, len(s)):
                substring = s[idx:i+1]
                if substring not in words:
                    continue
                strings = dfs(i+1)
                if not strings:
                    continue
                for substr in strings:
                    sentence = substring
                    if substr:
                        sentence += " " + substr
                    res.append(sentence)

            return res

        return dfs(0)
        