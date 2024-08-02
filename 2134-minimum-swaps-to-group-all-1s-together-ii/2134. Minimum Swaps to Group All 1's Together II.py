class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        num_1 = nums.count(1)
        n = len(nums)
        res = 1e9
        nums = nums + nums

        curr_0 = 0  
        for i in range(num_1): # Initialize window
            if nums[i] == 0:
                curr_0 += 1
        res = min(res, curr_0)

        for r in range(num_1, n + num_1):
            if nums[r-num_1] == 0:
                curr_0 -= 1
            if nums[r] == 0:
                curr_0 += 1
            res = min(res, curr_0)
        return res





        