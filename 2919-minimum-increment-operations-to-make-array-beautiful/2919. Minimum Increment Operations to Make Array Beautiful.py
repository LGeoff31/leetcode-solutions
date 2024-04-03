class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        #dp[i] = min increments to make subarray consisting first i nums beautiful, while having nums[i] >= k
        dp=[0] * len(nums)
        dp[0] = max(0, k - nums[0])
        dp[1] = max(0, k - nums[1])
        dp[2] = max(0, k - nums[2])

        for i in range(3, len(dp)):
            if nums[i] < k:
                dp[i] = max(0, k - nums[i] + min(dp[i-1], dp[i-2], dp[i-3]))
            else:
                dp[i] = min(dp[i-1], dp[i-2], dp[i-3])
        print(dp)
        return min(dp[-1], dp[-2], dp[-3])


        