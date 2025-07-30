class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        """
        greedy pick max 2, then smallest 1
        """
        res = 0
        nums.sort()
        l, r = 0, len(nums) - 1
        while l < r:
            res += nums[r-1]
            r -= 2
            l += 1
        return res