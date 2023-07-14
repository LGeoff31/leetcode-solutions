class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx_of_zero = 0
        for i in range(len(nums)):
            if nums[idx_of_zero] == 0 and nums[i] != 0:
                nums[idx_of_zero], nums[i] = nums[i], nums[idx_of_zero]
            if nums[idx_of_zero] != 0:
                idx_of_zero += 1
