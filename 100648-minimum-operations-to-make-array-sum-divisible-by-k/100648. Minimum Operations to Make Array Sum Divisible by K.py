class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        currSum = sum(nums)
        return currSum % k