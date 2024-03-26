class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.res = 0

        @cache
        def dfs(idx, currSum):
            res = 0
            if idx == len(nums) and currSum == target: return 1
            if idx != len(nums):
                res+=dfs(idx+1, currSum+nums[idx])
                res+=dfs(idx+1, currSum-nums[idx])
            return res
        return dfs(0, 0)
        # return self.res

        