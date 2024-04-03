class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        a,b = 0, len(nums) - 1
        while a <= b:
            mid = (a+b) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                b = mid - 1
            else:
                a = mid + 1
        return a
