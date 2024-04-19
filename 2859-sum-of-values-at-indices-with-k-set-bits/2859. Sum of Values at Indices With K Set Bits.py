class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        def bitCount(n):
            mask = 1
            res = 0
            for i in range(32):
                if mask & n: res+=1
                mask <<= 1
            return res
        res = 0
        for i in range(len(nums)):
            if bitCount(i) == k:
                res+=nums[i]
        return res
        