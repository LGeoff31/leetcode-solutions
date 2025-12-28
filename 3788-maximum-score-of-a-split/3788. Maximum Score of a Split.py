class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        suff = [-1e10] * len(nums)
        suff[-1] = nums[-1]
        for i in range(len(nums) -2, -1, -1):
            suff[i] = min(nums[i], suff[i+1])

        pref = 0
        res = -float('inf')
        for i in range(len(nums)-1):
            pref += nums[i]
            res = max(res, pref - suff[i+1])
        return res
