class Solution:
    def minOperations(self, nums: list[int]) -> int:
        """
        [5,1,2,3]
        +4
        [5,5,6,7]
        """
        curr = 0
        res = 0

        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                diff = nums[i-1] - nums[i]
                res += diff
                
        return res