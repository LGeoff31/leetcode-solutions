class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []

        def valid(num):
            for i in range(1, num + 1):
                if i | (i+1) == num:
                    return i
            return -1

        for n in nums:
            res.append(valid(n))
        return res