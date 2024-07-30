class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        if nums == sorted(nums) and len(nums) == len(set(nums)):
            return n*(n+1) // 2
        
        x = 0
        while x+1 < n and nums[x+1] > nums[x]:
            x += 1
        
        y = n-1
        while y >= 0 and nums[y] > nums[y-1]:
            y -= 1
        

        arr1, arr2 = nums[:x+1], nums[y:]

        res = 1 # Entire array
        for i in range(x+1):
            res += len(arr2) - bisect.bisect_right(arr2, arr1[i])
        res += len(arr1) + len(arr2)
        return res