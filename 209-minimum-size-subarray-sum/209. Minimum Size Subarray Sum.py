class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        minLength = 1e9
        currSum = 0
        while l < len(nums) and r < len(nums):
            currSum += nums[r]
            if currSum >= target:
                currLength = r - l + 1
                minLength = min(minLength, currLength)
                currSum -= nums[l]
                currSum -= nums[r]
                l += 1
            else:
                r += 1
        if minLength == 1e9: return 0
        return minLength
            


        