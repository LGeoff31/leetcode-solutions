from sortedcontainers import SortedList
class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        lst = SortedList()
        res = 1e9
        for i in range(x, len(nums)):
            lst.add(nums[i-x])
            insertIdx = lst.bisect_left(nums[i])

            if insertIdx > 0:
                res = min(res, nums[i] - lst[insertIdx-1])
            if insertIdx < len(lst):
                res = min(res, lst[insertIdx] - nums[i])
        return res
