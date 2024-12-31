class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2 == 1: return False
        goal = totalSum // 2

        # Find a subset that sums to goal
        @cache
        def dfs(idx, currSum):
            if currSum > goal:
                return False
            if currSum == goal:
                return True
            if idx >= len(nums):
                return False
            
            # # TAKE
            # if dfs(idx+1, currSum + nums[idx]): return True
            # # DONT TAKE
            # if dfs(idx+1, currSum): return True
            return dfs(idx+1, currSum + nums[idx]) or dfs(idx+1, currSum)
            
        return dfs(0 ,0)

        # nums.sort()
        # curr = 0
        # for num in nums:
        #     curr += num
        #     if curr == goal:
        #         return True
        #     elif curr > goal:
        #         return False
        # return False
        # if sum(nums) % 2 == 1: return False

        # targetSum = sum(nums) // 2
        # #Time: O(n^2)
        # #Memory: O(n)
        # dp = set()
        # dp.add(0)
        # for i in range(len(nums)):
        #     new_dp = set()
        #     for elem in dp:
        #         new_dp.add(elem)
        #         if elem + nums[i] <= targetSum:
        #             new_dp.add(elem + nums[i])
        #     dp = new_dp
        # return targetSum in dp



