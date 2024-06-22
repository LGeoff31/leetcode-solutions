class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0 and i+2 < len(nums):
                nums[i] = 1
                nums[i+1] = not nums[i+1]
                nums[i+2] = not nums[i+2]
                res += 1
            # print(nums)
        return res if sum(nums) == len(nums) else -1
        
        