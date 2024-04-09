from sortedcontainers import SortedList
from heapq import heapify, heappush, heappop
class Solution:
    def maxIncreasingGroups(self, nums: List[int]) -> int:
        l,r = 0, len(nums)
        res = 0
        lst=sorted(nums)
        n = len(nums)

        def possible(x):
            sub = [lst[0]]
            for i in range(1, n):
                sub.append(lst[i] - lst[i-1])
            for i in range(-x, 0, 1):
                sub[i] -= 1
            for i in accumulate(list(accumulate(sub))):
                if i < 0:
                    return False
            return True
        # print(possible(2))
        while l <= r:
            x = (l+r) // 2
            if possible(x):
                res = max(res, x)
                l = x + 1
            else:
                r = x-1
        
        return res

        