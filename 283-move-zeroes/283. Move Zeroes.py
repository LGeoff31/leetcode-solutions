class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lst = []
        for i in range(len(nums)):
            if nums[i] != 0:
                lst.append(nums[i])
        for i in range(nums.count(0)):
            lst.append(0)
        for i in range(len(nums)):
            nums[i] = lst[i]

       
            