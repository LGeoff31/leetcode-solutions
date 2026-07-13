class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        dp[i][j] = # palindromic substrings from s[i:j]
        if s[i-1] == s[j+1]: dp[i][j] = 

        """
        def expand(i, j):
            res = 0
            while i >= 0 and j < len(s) and s[i] == s[j]:
                res += 1
                i -= 1
                j += 1
            return res
        
        res = 0
        for i in range(len(s)):
            res += expand(i, i)
            res += expand(i, i+1)
        return res