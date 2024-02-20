class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if min(nums) + (sum(nums) - min(nums) - max(nums)) > max(nums):
            if nums[0] == nums[1] and nums[1] == nums[2]: return "equilateral"
            elif nums[0] == nums[1] or nums[1] == nums[2] or nums[0] == nums[2]: return "isosceles"
            else: return "scalene"
        else:
            return "none"

        