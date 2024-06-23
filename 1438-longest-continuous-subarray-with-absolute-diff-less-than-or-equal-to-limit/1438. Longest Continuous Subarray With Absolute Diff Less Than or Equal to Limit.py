from sortedcontainers import SortedList
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        lst = SortedList()
        l, r = 0, 0
        res = 0
        while r < len(nums):
            lst.add(nums[r])
            while l < len(nums) and lst[-1] - lst[0] > limit:
                lst.remove(nums[l])
                l += 1
            r+=1
            res = max(res, len(lst))

        return res
        