class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 0
        while i < len(nums) and j < len(nums):
            nums[j] = nums[i]
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            i += 1
            j += 1
        return len(set(nums))