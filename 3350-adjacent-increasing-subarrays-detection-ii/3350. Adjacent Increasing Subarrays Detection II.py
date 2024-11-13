class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        res = 0
        lst = []
        i = 0
        while i < len(nums):
            idx = i+1
            while idx < len(nums) and nums[idx] > nums[idx-1]:
                idx += 1
            lst.append([i, idx-1])
            i = idx
        print(lst)
        res = (1 + lst[0][-1] - lst[0][0]) // 2
        for i in range(1, len(lst)):
            res = max(res, 1 + min(lst[i][-1] - lst[i][0], lst[i-1][-1] - lst[i-1][0]))
            res = max(res, (1 + lst[i][-1] - lst[i][0]) // 2)
            
            print(res)

        return res