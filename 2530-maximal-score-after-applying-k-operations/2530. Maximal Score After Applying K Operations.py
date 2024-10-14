from sortedcontainers import SortedList
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        res = 0
        a = SortedList(nums)
        for i in range(k):
            res += a[-1]
            temp = a[-1]
            a.remove(a[-1])
            a.add(ceil(temp/3))
        return res