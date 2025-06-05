class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False 
        target_sum = sum(nums) // 2

        @cache
        def dfs(i, currSum):
            if i == len(nums):
                return currSum == target_sum
            
            return dfs(i+1, currSum + nums[i]) or dfs(i+1, currSum)    
        
        return dfs(0, 0)