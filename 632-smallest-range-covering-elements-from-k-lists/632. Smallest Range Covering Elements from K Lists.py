class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        lst = SortedList()
        for i in range(len(nums)):
            lst.add([nums[i][0], i, 0])
        start, end = lst[0][0], lst[-1][0]
        while True:
            val, idx, i = lst[0]
            lst.remove(lst[0])
            i += 1
            if i >= len(nums[idx]):
                return [start, end]
            lst.add([nums[idx][i], idx, i])
            if lst[-1][0] - lst[0][0] < end - start:
                start = lst[0][0]
                end = lst[-1][0]
        return []
        
