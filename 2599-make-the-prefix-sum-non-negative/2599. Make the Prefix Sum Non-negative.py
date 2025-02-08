class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        curr = 0
        res = 0
        maxNegative = 1e9
        lst = SortedList()
        for i in range(len(nums)):
            lst.add(nums[i])
            curr += nums[i]
            if curr < 0:
                res += 1
                curr -= lst[0]
                lst.remove(lst[0])
        return res