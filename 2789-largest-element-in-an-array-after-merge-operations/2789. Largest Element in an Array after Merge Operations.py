class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        i = len(nums) - 2
        res = 0
        currSum = 0
        while i >= 0:
            if not currSum:
                if nums[i] <= nums[i+1]:
                    currSum += nums[i] + nums[i+1]
                    i -= 1
                else:
                    i -= 1
            else:
                if nums[i] <= currSum:
                    currSum += nums[i]
                    i -= 1
                else:
                    currSum = nums[i]
                    i -= 1
        return max(currSum, max(nums))
            
            
        