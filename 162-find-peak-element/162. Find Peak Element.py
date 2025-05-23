class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        if len(nums) <= 2:
            return 0 if nums[0] > nums[1] else 1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            print('trying', mid)
            if mid != 0 and mid != len(nums) - 1:
                if nums[mid] > max(nums[mid-1], nums[mid+1]):
                    return mid
                elif nums[mid] > nums[mid-1]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if mid == 0:
                    if nums[mid] > nums[1]:
                        return 0
                    else:
                        l = mid + 1
                else:
                    if nums[mid] > nums[mid-1]:
                        return mid
                    else:
                        r= mid-1
                # return mid
                # return -1