class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res = 1
        curr = 0

        prev = -1
        for i in range(len(nums)):
            if nums[i] > prev:
                curr += 1
            else:
                curr = 1
            
            res = max(res, curr)
            prev = nums[i]
        return res