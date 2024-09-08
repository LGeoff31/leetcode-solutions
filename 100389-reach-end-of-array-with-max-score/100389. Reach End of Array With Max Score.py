class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        curr_num = nums[0]
        prev_idx = 0
        i = 1
        res = 0
        while i < len(nums):
            # If last index
            if i == len(nums) - 1:
                res += (i - prev_idx) * curr_num
                break
            if nums[i] > curr_num:
                res += (i - prev_idx) * curr_num
                prev_idx = i
                curr_num = nums[i]
                i += 1
            else:
                i += 1
        return res
