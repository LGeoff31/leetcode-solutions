class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        dp = [[0,0] for _ in range(n)]
        dp[1][0] = nums[0] - nums[1]
        dp[1][1] = nums[0] + nums[1]
        for i in range(2, n):
            dp[i][0] = dp[i-1][1] - nums[i]
            dp[i][1] = max(dp[i-1][0], dp[i-1][1]) + nums[i]
        print(dp)
        return max(dp[n-1])