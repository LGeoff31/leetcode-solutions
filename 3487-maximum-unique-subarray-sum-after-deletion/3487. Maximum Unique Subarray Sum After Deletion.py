class Solution:
    def maxSum(self, nums: List[int]) -> int:
        dic = set(nums)
        if all(key < 0 for key in dic): return max(nums)
        return sum(key for key in dic if key > 0)