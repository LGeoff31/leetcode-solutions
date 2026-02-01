class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        a = nums.copy()
        nums.remove(a[0])
        nums.sort()
        return a[0] + sum(nums[:2])