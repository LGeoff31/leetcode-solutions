class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], k: int) -> bool:
        return max(Counter(nums).values()) * k <= len(nums)