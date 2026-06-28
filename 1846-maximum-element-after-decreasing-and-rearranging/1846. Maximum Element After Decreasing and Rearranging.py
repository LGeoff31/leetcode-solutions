class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        res = 1
        i = 1
        prev = 1
        while i < len(arr):
            if arr[i] != prev:
                res += 1
                prev += 1
            i += 1
        return res