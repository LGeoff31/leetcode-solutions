class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        prefix = [0] * len(nums)
        for l,r in queries:
            prefix[l] -= 1
            if r+1 < len(prefix):
                prefix[r+1] += 1
        prefix = list(accumulate(prefix))
        for i in range(len(nums)):
            nums[i] += prefix[i]
        return sum(num > 0 for num in nums) == 0