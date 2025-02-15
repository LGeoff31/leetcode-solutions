class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1 # 0, 5
        while l <= r:
            mid = l + (r-l) // 2 #2
            if mid == 0: # Very left
                l = mid + 1
                continue
            if arr[mid] > max(arr[mid-1], arr[mid+1]):
                return mid
            elif arr[mid] > arr[mid-1] and arr[mid] < arr[mid+1]:
                l = mid + 1
            else:
                r = mid - 1
        return "hahaha"