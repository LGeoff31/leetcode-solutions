class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = abs(nums[i])
        nums.sort(reverse=True)
        positive, negative = 0, 0
        for i in range(ceil(len(nums) / 2)):
            positive += nums[i] ** 2

        for i in range(ceil(len(nums) / 2), len(nums)):
            negative += nums[i] ** 2

        return positive - negative