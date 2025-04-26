class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        left, right, bad = -1, -1, -1
        res = 0
        for i, num in enumerate(nums):
            if not minK <= num <= maxK:
                bad = i
            if num == minK: left = i
            if num == maxK: right = i
            res += max(0, min(left, right) - bad)
        return res