class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10 ** 9 + 7

        freq = [{} for _ in range(len(words[0]))]
        for word in words:
            for i, char in enumerate(word):
                freq[i][char] = freq[i].get(char, 0) + 1
    
        @cache
        def dfs(i, j):
            if j == len(target):
                return 1
            if i >= len(freq):
                return 0
            # DONT TAKE
            res = dfs(i+1, j)
            # TAKE
            if target[j] in freq[i]:
                res += freq[i][target[j]] * dfs(i+1, j+1)
            return res % MOD

        return dfs(0, 0)