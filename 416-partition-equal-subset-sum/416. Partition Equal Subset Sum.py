class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1: return False

        targetSum = sum(nums) // 2

        #What are we caching???
        #If we reach a idx and currSum which we know is fale we can cache that
        @cache
        def dfs(idx, currSum):
            if currSum == targetSum: 
                return True
            if idx >= len(nums):
                return False
            
            return dfs(idx+1, currSum) or dfs(idx+1, currSum + nums[idx])


        return dfs(0, 0)


        