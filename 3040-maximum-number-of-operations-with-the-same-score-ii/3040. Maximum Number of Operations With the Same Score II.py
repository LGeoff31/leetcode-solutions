class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        @cache 
        def dfs(i, j, target): #i: start, j: end
            if j-i+1 < 2:
                return (n- (j-i+1)) // 2
            if nums[i] + nums[i+1] != target and nums[j] + nums[j-1] != target and nums[i] + nums[j] != target:
                return (n- (j-i+1)) // 2
            res = 0
            # First two
            if nums[i] + nums[i+1] == target:
                res = max(res, dfs(i+2, j, target))
            
            # Last two
            if nums[j] + nums[j-1] == target:
                res = max(res, dfs(i, j-2, target))
            
            # First + last
            if nums[i] + nums[j] == target:
                res = max(res, dfs(i+1, j-1, target))
            return res
        res = 0
        res = max(res, dfs(2, n-1, nums[0] + nums[1]))
        res = max(res, dfs(0, n-3, nums[-1] + nums[-2]))
        res = max(res, dfs(1, n-2, nums[0] + nums[-1]))
        return res
