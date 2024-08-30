from sortedcontainers import SortedList
class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        a,b = SortedList(), SortedList()
        for i in range(n - 2):
            a.add(nums[i])
        b.add(nums[-1])
        arr = [False] * (n-2)
        for i in range(n-2, 0, -1): # [0, 5] -> [1,2,3,4]
            if nums[i] < b[0] and nums[i] > a[-1]:
                arr[i-1] = True
            b.add(nums[i])
            a.remove(nums[i-1])
        print(arr)
        res = 0
        for i in range(1, n-1):
            if arr[i-1]:
                res += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                res += 1
        return res
        