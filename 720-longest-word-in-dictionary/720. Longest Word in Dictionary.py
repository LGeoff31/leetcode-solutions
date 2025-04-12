class Solution:
    def longestWord(self, words: List[str]) -> str:
        visited = set()
        words_set = set(words)
        res = ""

        @cache
        def dfs(word):
            nonlocal res
            if not word:
                return True
            if word not in words_set:
                return False

            if dfs(word[:-1]):
                print(word)
                if len(word) == len(res):
                    if word < res:
                        res = word
                elif len(word) > len(res):
                    res = word
                return True
            return False
        
        for word in words:
            dfs(word)
            print(res)
        return res