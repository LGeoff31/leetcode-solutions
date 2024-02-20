class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if len(nums) == 1 and nums[0] == 0:
            return 1
        if len(nums) == 1 and nums[0] == 1:
            return 0
        expected_sum = (len(nums)) * (len(nums)+1) // 2
        return expected_sum - sum(nums)