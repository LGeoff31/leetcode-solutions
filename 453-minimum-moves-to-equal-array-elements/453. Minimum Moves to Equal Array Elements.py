from sortedcontainers import SortedList
class Solution:
    def minMoves(self, nums: List[int]) -> int: 
        n = len(nums)
        nums.sort()
        return sum(nums) - n * nums[0]