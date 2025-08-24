class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if nums.count(1) == len(nums): return len(nums) - 1
        @cache
        def dfs(i, used):
            if i == len(nums):
                return 0
            if nums[i] == 1:
                return 1 + dfs(i+1, used)
            if used:
                return 0
            return dfs(i+1, True)

        res = 0
        for i in range(len(nums)):
            res = max(res, dfs(i, False))
        return res