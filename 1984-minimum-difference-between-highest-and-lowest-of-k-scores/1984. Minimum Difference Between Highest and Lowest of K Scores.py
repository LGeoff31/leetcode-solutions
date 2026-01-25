class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        res = 1e9
        nums.sort()
        for i in range(len(nums) - k + 1):
            subarr = nums[i: i+k]
            res = min(res, max(subarr) - min(subarr))
        return res