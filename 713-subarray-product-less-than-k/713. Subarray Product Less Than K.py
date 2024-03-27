class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        i = 0
        a = 1

        for j in range(len(nums)):
            a *= nums[j]
            while i <= j and a >= k:
                a /= nums[i]
                i += 1
            res+=j-i+1
        return res
