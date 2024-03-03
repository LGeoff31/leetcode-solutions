class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[1e9] * (len(word2)+1) for i in range(len(word1) + 1)]

        for r in range(len(word1)+1):
            dp[r][len(word2)] = len(word1) - r

        for c in range(len(word2)+1):
            dp[len(word1)][c] = len(word2) - c
        
        for r in range(len(word1)-1, -1, -1):
            for c in range(len(word2)-1, -1, -1):
                if word1[r] == word2[c]:
                    dp[r][c] = dp[r+1][c+1]
                else:
                    dp[r][c] = 1 + min(dp[r+1][c+1], dp[r][c+1], dp[r+1][c])
        return dp[0][0]


        return -1
        