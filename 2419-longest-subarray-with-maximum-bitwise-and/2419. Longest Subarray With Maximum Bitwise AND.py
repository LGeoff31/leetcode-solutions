class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_ans = max(nums)
        count = 0
        res = 0
        for n in nums:
            if n == max_ans:
                count += 1
            else:
                count = 0
            res = max(res, count)
        return res