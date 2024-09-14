class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        a = max(nums)
        res = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == a:
                count += 1
                res = max(res, count)
            else:
                count = 0
        return res

        # return nums.count(max(nums))
        