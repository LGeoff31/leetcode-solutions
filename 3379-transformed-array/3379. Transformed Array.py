class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        res = []
        for i, n in enumerate(nums):
            res.append(nums[(i+n) % len(nums)])
        return res