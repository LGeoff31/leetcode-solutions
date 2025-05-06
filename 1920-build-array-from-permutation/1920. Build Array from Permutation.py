class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        for i,num in enumerate(nums):
            res[i] = nums[num]
        return res