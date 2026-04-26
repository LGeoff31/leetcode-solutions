class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        res = [nums[0]]
        for i in range(1, len(nums) - 1):
            if nums[:i] and nums[i] > max(nums[:i]) or nums[i+1:] and nums[i] > max(nums[i+1:]):
                res.append(nums[i])
        if len(nums) > 1:
            res.append(nums[-1])
        return res
            
        