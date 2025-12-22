class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        dp = [1] * len(strs[0])
        kept = 1
        for i in range(len(strs[0]) -2, -1, -1):
            for j in range(i+1, len(strs[0])):
                for row in strs:
                    if row[i] > row[j]:
                        break
                else:
                    dp[i] = max(dp[i], 1 + dp[j])
            kept = max(kept, dp[i])
        return len(strs[0]) - kept
