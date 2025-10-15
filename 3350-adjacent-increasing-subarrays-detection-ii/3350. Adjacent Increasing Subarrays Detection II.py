class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        lst = [0] * n
        lst[-1] = 1
        curr = 1
        for i in range(len(nums) -2, -1, -1):
            if nums[i] < nums[i+1]:
                curr += 1
            else:
                curr = 1
            lst[i] = curr
        print(lst)
        res = 0
        for i in range(len(lst)):
            length_arr1 = lst[i]
            res = max(res, length_arr1 // 2)
            if i + length_arr1 < len(lst):
                length_arr2 = lst[i + length_arr1]
                res = max(res, min(length_arr1, length_arr2), max(length_arr1, length_arr2) // 2)
        return res
