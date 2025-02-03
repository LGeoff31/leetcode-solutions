class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        def longest_increasing(start, arr):
            count = 1
            for i in range(1, len(arr)):
                if arr[i] > arr[i - 1]:
                    count += 1
                else:
                    return count
            return count
        res = 0
        for i in range(len(nums)):
            res = max(res, longest_increasing(i, nums[i:]))
            res = max(res, longest_increasing(i, nums[:i+1][::-1]))
            print(res)
        return res