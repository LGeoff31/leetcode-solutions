class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i, j = 0, 0
        for k in range(1, len(nums)):
            if nums[k] < nums[i]:
                i = k
            if j == 0 and nums[k] > nums[i]:
                j = k
            if nums[k] < nums[j] and nums[k] > nums[i]:
                j = k
                
            if nums[k] > nums[j]:
                return True
        return False


        