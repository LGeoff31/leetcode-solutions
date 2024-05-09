class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = len(nums) -1, len(nums) - 1

        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        
        if i == 0:
            nums.reverse()
            return
        # i = 3, j = 2
        #[1,3,4,2] -> [1,4,2,3]

        #[1,4,3,2]
        while nums[j] <= nums[i-1]:
            j -= 1
        nums[i-1], nums[j] = nums[j], nums[i-1]
        nums[i:] = nums[len(nums) - 1 : i-1: -1]
