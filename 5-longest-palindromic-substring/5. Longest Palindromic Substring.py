class Solution:
    def longestPalindrome(self, s: str) -> str:

        dp = [[False] * len(s) for _ in range(len(s))]
        
        for i in range(len(s)):
            dp[i][i] = True

        longestSubstring = s[0]
        for r in range(len(s)-2, -1, -1):
            for c in range(r+1, len(s)):
                if s[r] == s[c]:
                    if c-r == 1 or dp[r+1][c-1]:
                        dp[r][c] = True
                        if c-r+1 > len(longestSubstring):
                            longestSubstring = s[r:c+1] #very slow
        return longestSubstring

         