class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1: return False

        targetSum = sum(nums) // 2

        dp = set()
        dp.add(0)
        for i in range(len(nums)):
            new_dp = set()
            for elem in dp:
                new_dp.add(elem)
                new_dp.add(elem + nums[i])
            dp = new_dp
        return targetSum in dp



