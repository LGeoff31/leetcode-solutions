class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        res = -1
        a = Counter(nums)
        for key in a:
            if a[key] == 1:
                res = max(res, key)
        return res
        