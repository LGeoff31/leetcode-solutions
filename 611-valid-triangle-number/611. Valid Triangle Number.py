class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """
        Triangle Inequality: |A+B| <= |A| + |B|
        """
        res = 0
        nums.sort()
        n = len(nums)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                max_longest_side = nums[i] + nums[j]
                res += max(0, bisect_left(nums, max_longest_side) - j - 1)
        return res