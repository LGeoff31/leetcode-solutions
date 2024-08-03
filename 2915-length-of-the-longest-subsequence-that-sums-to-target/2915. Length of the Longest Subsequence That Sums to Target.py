class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)
        @cache
        def dfs(i, val): #val can only be up 1000
            if val == target:
                return 0
            if i >= n or val > target:
                return -1e9
            return max(1 + dfs(i+1, val+nums[i]), dfs(i+1, val))
        ans = dfs(0,0)
        dfs.cache_clear()
        if ans < -1000:
            return -1
        return ans