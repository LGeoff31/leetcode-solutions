class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        res = 0
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                valid = target - nums[i] - nums[j]  - 1# 2 - 0 + 2 = 4 
                idx = bisect_right(nums, valid)
                res += max(idx - j - 1, 0)
        return res