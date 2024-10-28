class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        visited = set(nums)
        res = -1
        @cache
        def dfs(num):
            if num not in visited:
                return 0
            return 1 + dfs(num * num)
        for i in range(len(nums)):
            total = dfs(nums[i])
            if total != 1:
                res = max(res, dfs(nums[i]))
        return res