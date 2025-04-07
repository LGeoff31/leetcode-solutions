class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0: return False
        target = sum(nums) // 2
        # 100 * 200 = 20,000 which is pretty small lol
        @cache
        def dfs(i, currSum): #O(n^)
            if currSum == target:
                return True
            if i == len(nums) or currSum > target:
                return False

            return dfs(i+1, currSum + nums[i]) or dfs(i+1, currSum)
        return dfs(0, 0)