class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        maxHeap = []
        lst = SortedList()
        for num in nums:
            lst.add(num)
        i = len(nums) - 1
        res = 0
        while i >= 0:
            currMax = -1
            if lst:
                currMax = lst[-1]
                lst.remove(lst[-1])
            while i>=0 and nums[i] != currMax:
                lst.remove(nums[i])
                i -= 1
                res += 1
            i -= 1
        return len(nums) - res
            