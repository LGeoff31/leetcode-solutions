class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        prefix = [0] * (len(nums) + 1)
        for l, r in queries:
            prefix[l] += 1
            prefix[r + 1] -= 1
        prefix = list(accumulate(prefix))
        res = True
        for i in range(len(nums)):
            res = res and nums[i] <= prefix[i]
        return res