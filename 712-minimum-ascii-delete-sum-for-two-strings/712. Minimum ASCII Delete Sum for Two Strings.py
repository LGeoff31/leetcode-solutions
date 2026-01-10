class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        def ascii_sum(word):
            return sum(ord(c) for c in word)
        print(ord('s'))
        @cache
        def dfs(i, j):
            if i >= len(s1) or j >= len(s2):
                return ascii_sum(s1[i:]) + ascii_sum(s2[j:])
            
            res = 1e9
            if s1[i] == s2[j]:
                res = min(res, dfs(i+1, j+1))
            res = min(res, ord(s1[i]) + dfs(i+1, j), ord(s2[j]) + dfs(i, j+1), ord(s1[i]) + ord(s2[j]) + dfs(i+1, j+1))
            return res
        return dfs(0, 0)