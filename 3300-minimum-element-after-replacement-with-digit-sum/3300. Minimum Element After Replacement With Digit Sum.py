class Solution:
    def minElement(self, nums: List[int]) -> int:
        def convert(num):
            res = 0
            for i in str(num):
                res += int(i)
            return res
        res = 1e9
        for i in nums:
            res = min(res, convert(i))
        return res