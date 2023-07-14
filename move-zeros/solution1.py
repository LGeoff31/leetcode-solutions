class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def check_complete():
            num_zeros = nums.count(0)
            for i in range(len(nums)-num_zeros):
                if nums[i] == 0:
                    return False
            return True
        
        while not check_complete():
            for i in range(len(nums) - 1):
                if nums[i] == 0 and nums[i+1] != 0:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
             

       
            