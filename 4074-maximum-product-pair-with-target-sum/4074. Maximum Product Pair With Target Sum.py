class Solution:
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
        res = [-1, -1]
        product = -float('inf')

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j: continue
                if nums[i] + nums[j] == target and nums[i] > nums[j]:
                    if nums[i] * nums[j] > product:
                        product = nums[i] * nums[j]
                        res = [i, j]
        return res