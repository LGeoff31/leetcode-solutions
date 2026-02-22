class Solution:
    def countSequences(self, nums: List[int], k: int) -> int:
        @cache
        def dfs(i, curr):
            if i == len(nums):
                return isclose(curr, k)
                
            if i > len(nums):
                return 0

            return dfs(i+1, curr) + dfs(i+1, curr * nums[i]) + dfs(i+1, curr / nums[i])
            
        return dfs(0, 1)