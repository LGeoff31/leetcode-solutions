class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        nums.sort()
        res = 0
        l, r = 0, 1
        print(nums)
        while r < len(nums):
            # if nums[l] == nums[r]:
            #     nums[r] += 1
            #     res += 1
            if nums[r] <= nums[l]:
                res += (nums[l] - nums[r] + 1)
                nums[r] += (nums[l] - nums[r] + 1)
            # while nums[r] <= nums[l]:
            #     nums[r] += 1
            #     res += 1
            l += 1
            r += 1
        return res
