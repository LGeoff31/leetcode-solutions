class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.res = []
        words = set(wordDict)

        def dfs(idx, currWords):
            if idx == len(s):
                self.res.append(currWords)

            for i in range(idx, len(s)):
                substring = s[idx:i+1]
                if substring in words:
                    print(i+1, currWords + substring)
                    if currWords == "":
                        dfs(i+1, substring)
                    else:
                        dfs(i+1, currWords + " " + substring)
        dfs(0, "")
        return self.res
        