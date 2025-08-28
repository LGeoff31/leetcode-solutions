class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        target = nums[0]
        for n in nums[1:]:
            target &= n
        if target != 0: return 1
        res = 0
        bit = nums[0]
        for n in nums[1:]:
            if bit == target:
                res += 1
                bit = n
            bit &= n
        if bit == target:
            res += 1
        return res