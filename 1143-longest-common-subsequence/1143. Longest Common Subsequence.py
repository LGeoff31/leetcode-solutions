class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        dp[i][j] = max common subsequence (text1[:i], text2[:j]) 

        if text1[i] == text2[j]:
            dp[i][j] = 1 + dp[i-1][j-1]
        else
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        base cases
        dp[0][...] = 0
        dp[...][0] = 0

        """
        n, m = len(text1), len(text2)
        dp = [[0] * (m+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
