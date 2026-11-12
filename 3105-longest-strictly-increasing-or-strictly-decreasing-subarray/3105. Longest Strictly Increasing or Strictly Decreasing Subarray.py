class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                subarr = nums[i: j + 1]

                if (subarr == sorted(subarr) or subarr == sorted(subarr, reverse=True)) and len(subarr) == len(set(subarr)):
                    res = max(res, len(subarr))
        return res