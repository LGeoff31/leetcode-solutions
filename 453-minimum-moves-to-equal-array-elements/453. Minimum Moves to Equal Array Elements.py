class Solution:
    def minMoves(self, nums: list[int]) -> int:
        a = min(nums)
        res = 0
        for n in nums:
            res += n - a
        return res