class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text1)+1) for _ in range(len(text2)+1)]
        for c in range(len(text1)):
            dp[-1][c] = 0
        for r in range(len(text2)):
            dp[r][-1] = 0
        
        for r in range(len(text2)-1, -1, -1):
            for c in range(len(text1)-1, -1, -1):
                if text2[r]==text1[c]:
                    dp[r][c] = 1 + dp[r+1][c+1]
                else:
                    dp[r][c] = max(dp[r+1][c], dp[r][c+1])
        return dp[0][0]

        print(dp)
        return 0
        