class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        global_res = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                res += 1
                global_res = max(global_res, res)
            else:
                res = 0
        return global_res