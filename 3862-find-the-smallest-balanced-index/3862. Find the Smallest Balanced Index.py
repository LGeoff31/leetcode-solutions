class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        if len(nums) == 1: return -1
        l = sum(nums)
        r = 1
        for i in reversed(range(len(nums))):
            l -= nums[i]
            if l == r: return i
            r *= nums[i]
        # prefix = [0] + list(accumulate(nums)) # [0, 2, 3, 5]
        # prefix = prefix[:-1]
        # suffix = [1] * (len(nums)) # [1,2,1]
        # suffix[-2] = nums[-1]
        # for i in range(len(suffix) - 3, -1, -1):
        #     suffix[i] = nums[i+1] * suffix[i+1]
    

        # for i in range(len(nums)):
        #     if prefix[i] == suffix[i]:
        #         return i
        return -1