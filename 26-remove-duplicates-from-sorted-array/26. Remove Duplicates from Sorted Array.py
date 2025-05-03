class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        correct_idx = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[correct_idx] = nums[i]
                correct_idx += 1
        return correct_idx