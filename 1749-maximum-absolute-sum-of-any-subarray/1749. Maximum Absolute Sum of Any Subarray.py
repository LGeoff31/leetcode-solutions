class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        res1 = 0
        res2 = 0

        # Case 1: abs(positive)
        local_res1 = 0
        for i in range(len(nums)):
            local_res1 = max(local_res1 + nums[i], 0)
            res1 = max(res1, local_res1)
        
        # Case 2: abs(negative)
        for i in range(len(nums)):
            nums[i] = -nums[i]
        local_res2 = 0
        for i in range(len(nums)):
            local_res2 = max(local_res2 + nums[i], 0)
            res2 = max(res2, local_res2)
        return max(res1, res2)
        

