class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        diff = -1e9

        for i in range(1, len(nums)):
            diff = max(diff, abs(nums[i] - nums[i-1]))
        return max(diff, abs(nums[0] - nums[-1]))