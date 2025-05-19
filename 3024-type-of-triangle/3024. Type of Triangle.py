class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if not(max(nums) < sum(nums) - max(nums)): return "none"
        if len(set(nums)) == 1:
            return 'equilateral'
        if len(set(nums)) == 2:
            return "isosceles"
        return "scalene"