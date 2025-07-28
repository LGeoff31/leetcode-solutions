class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for n in nums:
            max_or = max_or | n
        @cache
        def dfs(i, curr):
            if i == len(nums):
                return curr == max_or
            
            return dfs(i+1, curr | nums[i]) + dfs(i+1, curr)
        return dfs(0, 0)
        