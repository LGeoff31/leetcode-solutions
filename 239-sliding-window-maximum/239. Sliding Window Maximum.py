class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        lst = SortedList()
        for i in range(k):
            lst.add(nums[i])

        res.append(lst[-1])
        for i in range(k, len(nums)):
            lst.remove(nums[i-k])
            lst.add(nums[i])
            res.append(lst[-1])

        return res