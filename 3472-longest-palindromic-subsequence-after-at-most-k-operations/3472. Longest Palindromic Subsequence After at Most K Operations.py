class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        def dist(a,b):
            return min(abs(ord(a) - ord(b)), 26-abs(ord(a) - ord(b)))
        @cache
        def dfs(i, j, k): #O(n^2 * k)
            if k < 0:
                return -1e9
            if i > j:
                return 0
            if not (0 <= i < len(s) and 0 <= j < len(s)):
                return -1e9
            if i == j:
                return 1
            
            return max(dfs(i+1, j, k), dfs(i, j-1, k), 2+dfs(i+1, j-1, k - dist(s[i], s[j])))
        print(dfs(2, 3, 0))
        return dfs(0, len(s) -1, k)