class Solution:
    def isGood(self, nums: List[int]) -> bool:
        return sorted(nums) == list(range(1, len(nums))) + [len(nums) - 1]