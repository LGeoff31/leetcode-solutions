from sortedcontainers import SortedList
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        lst = SortedList()
        res = []
        for i in range(k):
            lst.add(nums[i])
        if k % 2 == 0:
            res.append((lst[len(lst) // 2] + lst[len(lst) // 2 - 1]) / 2) 
        else:
            res.append(lst[len(lst) // 2])
        idx = k
        l = 0
        while idx < len(nums):
            lst.remove(nums[l])
            lst.add(nums[idx])
            if k % 2 == 0:
                res.append((lst[len(lst) // 2] + lst[len(lst) // 2 - 1]) / 2) 
            else:
                res.append(lst[len(lst) // 2])
            idx += 1
            l += 1
        return res