class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        prefix = list(accumulate(nums))
        res = 0
        for i in range(len(nums) - 1):
            if prefix[i] >= totalSum - prefix[i]:
                res += 1
        return res