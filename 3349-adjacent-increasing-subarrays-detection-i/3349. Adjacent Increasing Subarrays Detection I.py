class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        def increasing(arr):
            for i in range(1, len(arr)):
                if arr[i] <= arr[i-1]:
                    return False
            return True
        for i in range(len(nums) - k):
            arr1 = nums[i: i+k]
            arr2 = nums[i+k: i+2*k]
            if len(arr2) != len(arr1): return False
            if increasing(arr1) and increasing(arr2):
                return True
        return False
