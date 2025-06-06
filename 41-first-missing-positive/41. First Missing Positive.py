class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:   
        """
        Negative numebrs do not imapct the result.
        If you come across a positive value, mark the corresponding index as negative
        Loop through nums, if you come across a positive value, that means it hasn't been seen before so return its value
        """
        # [1,3,4]
        # Hey we're missing index 2
        nums = [a for a in nums if a > 0]
        n = len(nums) 
        for i in range(n):
            idx = abs(nums[i]) - 1
            if idx < len(nums) and nums[idx] > 0:
                nums[idx] *= -1

        for i in range(len(nums)):
            if nums[i] > 0:
                return i+1
        return len(nums) + 1