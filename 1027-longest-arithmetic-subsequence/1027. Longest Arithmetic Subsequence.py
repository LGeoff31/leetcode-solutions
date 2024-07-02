class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = [[0] * 1001 for _ in range(1001)] #dp[i][j] = max arthmetic subsequence with currNum with difference j


        for num in nums:
            for diff in range(-500, 501):
                # if num - diff >= 0:
                dp[num][diff] = max(dp[num][diff], 1 + dp[num - diff][diff])
        res = 0
        for arr in dp:
            res = max(res, max(arr))
        return res
        