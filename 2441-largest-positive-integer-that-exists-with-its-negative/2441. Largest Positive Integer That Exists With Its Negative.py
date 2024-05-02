class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        a = -1

        for i in range(len(nums)):
            if -1 * nums[i] in nums:
                a = max(a, nums[i])
        return a