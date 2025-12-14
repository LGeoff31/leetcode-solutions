class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        return sum(nums[len(nums) - k:]) - sum(nums[:k])