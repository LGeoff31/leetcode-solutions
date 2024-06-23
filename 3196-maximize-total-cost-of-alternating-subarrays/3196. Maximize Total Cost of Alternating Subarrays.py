class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        # If you end on a negative, the next has to be positive
        # If you end on a positive, the next can be positive or negative

        #[2, -4, -5, ] -> 3

        # DP???
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        dp = [[0,0] for _ in range(n)]
        print(n, dp, nums)
        dp[1][0] = nums[0] + nums[1] # Max if ith element wasn't flipped
        dp[1][1] = nums[0] - nums[1] # Max if ith element was flipped
        for i in range(2, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]) + nums[i]
            dp[i][1] = dp[i-1][0] - nums[i]
        return max(dp[n-1][0], dp[n-1][1])

        