class Solution:
    def findMin(self, nums: List[int]) -> int:  
        # The minimum element will be greater than left element and smaller than the right element
        # If that doesn't exist, the minimum element will either be the first or last element
        """
        [4,5,6,7,8,9,10,11,12,0,1,2,3]
        [1,2,3,4,5]
        """
        if len(nums) <= 2:
            return min(nums)
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            print('tryihng', mid)
            # if mid == 0 or mid == len(nums) - 1:
            #     return nums[mid]
            
            if (mid!=0 and mid!=len(nums)-1) and nums[mid] < nums[mid-1] and nums[mid] < nums[mid+1]:
                return nums[mid]
            elif nums[mid] > nums[-1]:
                l = mid + 1
            else:
                r = mid - 1
        return min(nums[0], nums[-1])
