class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        if sum([num < 0 for num in nums]) == len(nums): return min(nums) * min(nums)
        
        dp = [[-1e9,-1e9] for _ in range(len(nums))] # dp[i][0] = maximum subarr including nums[i] w/o squaring

        dp[0][0] = max(nums[0], 0)
        dp[0][1] = nums[0] * nums[0]

        res = min(nums)
        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i-1][0] + nums[i], nums[i])
            dp[i][1] = max(nums[i] * nums[i], dp[i-1][0] + nums[i] ** 2, dp[i-1][1] + nums[i])
        for a,b in dp:
            res = max(res, a, b)
        return res