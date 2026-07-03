class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        lst = SortedList()
        res = float('inf')

        for i in range(x, len(nums)):
            lst.add(nums[i])
    
        for i in range(len(nums) - x):
            val = nums[i]
            closest_idx = bisect_left(lst, val)
            if 0 <= closest_idx < len(lst): res = min(res, abs(val - lst[closest_idx]))
            if 0 <= closest_idx-1 < len(lst): res = min(res, abs(val - lst[closest_idx-1]))
            if 0 <= closest_idx+1 < len(lst): res = min(res, abs(val - lst[closest_idx+1]))
            lst.remove(nums[i+x])
        return res