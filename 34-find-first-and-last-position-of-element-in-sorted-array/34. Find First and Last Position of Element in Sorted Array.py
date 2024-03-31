from bisect import bisect_left
from bisect import bisect_right

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(target):
            l, r = 0, len(nums) -1
            while l <=r:
                mid = (l+r)//2
                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return False
        if binary_search(target):
            return [bisect_left(nums, target), bisect_right(nums, target) - 1]
        return [-1, -1]