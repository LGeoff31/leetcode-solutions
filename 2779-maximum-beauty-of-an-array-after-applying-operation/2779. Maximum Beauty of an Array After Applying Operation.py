class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums)):
            maxNum = nums[i] + 2 * k
            idx = bisect_right(nums, maxNum)
            res = max(res, idx - i)
        return res