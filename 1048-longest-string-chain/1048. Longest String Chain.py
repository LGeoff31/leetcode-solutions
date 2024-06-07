class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def possible(word1, word2):
            if len(word1) +1 != len(word2):
                return False
            i = j = 0
            mismatch = False
            while i < len(word1):
                if word1[i] == word2[j]:
                    i += 1
                    j += 1
                else:
                    if mismatch:
                        return False
                    j += 1
                    mismatch = True
            return True
        @cache
        def dfs(idx):
            res = 1
            for i in range(len(words)):
                if possible(words[idx], words[i]):
                    res = max(res, 1 + dfs(i))
            return res
        res = 0
        for i in range(len(words)):
            res = max(res, dfs(i))
        return res

         
        