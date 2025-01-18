class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        nums = nums + nums
        res = 0
        for i in range(1, n+1):
            res = max(abs(nums[i]-nums[i-1]), res)
        return res