class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if sum([num < 0 for num in nums]) == len(nums): return max(nums)
        res = 0
        curr = 0
        idx = 0
        while idx < len(nums):
            curr += nums[idx]
            if curr < 0:
                curr = 0
            idx += 1
            res = max(res, curr)
        return res