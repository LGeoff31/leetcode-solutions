class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        @cache
        def dfs(i, add):
            if i == len(nums):
                return 0
            res = 0
            # TAKE
            if add:
                res = max(res, dfs(i+1, not add) + nums[i])
            else:
                res = max(res, dfs(i+1, not add) - nums[i])
            # DONT TAKE
            res = max(res, dfs(i+1, add))
            return res
        
        return dfs(0, True)