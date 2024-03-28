class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:    
        if max(nums) < 0: return max(nums)
        maxSum = 0
        currMaxSum = 0
        minSum = 1e9
        currMinSum = 1e9
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            currMaxSum = max(currMaxSum + nums[i], nums[i]) #can either add elements or start new
            maxSum = max(maxSum, currMaxSum)
            currMinSum = min(currMinSum + nums[i], nums[i])
            minSum = min(minSum, currMinSum)
        return max(maxSum, total - minSum)
