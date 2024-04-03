class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #partition so both left and right side are sorted
        left, right = 0, len(nums) - 1
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1

        while True:
            partition = (left + right) // 2
            if nums[0] <= nums[partition] and nums[partition+1] <= nums[-1]:
                break
            elif nums[0] > nums[partition]:
                right = partition
            elif nums[partition+1] > nums[-1]:
                left = partition + 1
        
        #binary search left partition
        left, right = 0, partition 
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        #binary search right partition
        left, right = partition + 1, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
            



        