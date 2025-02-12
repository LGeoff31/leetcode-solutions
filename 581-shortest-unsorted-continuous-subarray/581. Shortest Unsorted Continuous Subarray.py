class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        a = sorted(nums)
        print(nums, a)
        start, end = 1e9, -1e9
        for i in range(len(nums)):
            if a[i] != nums[i]:
                start = min(start, i)
                end = max(end, i)
        return end-start+1 if start+1 < 100000 else 0