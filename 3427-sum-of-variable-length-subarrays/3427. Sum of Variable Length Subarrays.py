class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            start = max(0, i - nums[i])
            subarr = nums[start : i+1]
            res += sum(subarr)
        return res