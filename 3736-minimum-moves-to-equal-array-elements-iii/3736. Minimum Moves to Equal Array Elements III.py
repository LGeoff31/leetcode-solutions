class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_val = max(nums)
        return sum(abs(n - max_val) for n in nums)