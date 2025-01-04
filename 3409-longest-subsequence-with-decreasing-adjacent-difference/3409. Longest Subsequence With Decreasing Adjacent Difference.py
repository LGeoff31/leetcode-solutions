class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        # dp[i][diff] = longest valid subsequence ending with nums[i] and difference diff
        n = len(nums)
        dp = {}

        for i, num in enumerate(nums):
            best = 1
            for diff in range(300, -1, -1):
                if num + diff < 301:
                    if (num + diff, diff) in dp:
                        best = max(best, 1 + dp[(num+diff, diff)])
                if num - diff >= 0:
                    if (num - diff, diff) in dp:
                        best = max(best, 1 + dp[(num-diff, diff)])
                dp[(num, diff)] = best
        return max(dp.values())
                
