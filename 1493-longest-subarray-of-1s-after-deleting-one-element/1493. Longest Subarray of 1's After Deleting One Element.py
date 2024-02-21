class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if nums.count(1) == len(nums): return len(nums) - 1
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                l, r = i-1, i+1
                countLeft = 0
                countRight = 0
                while l >= 0 and nums[l] == 1:
                    l -= 1
                    countLeft += 1
                while r < len(nums) and nums[r] == 1:
                    r += 1
                    countRight += 1
                res = max(res, countRight + countLeft)
                
        return res
        