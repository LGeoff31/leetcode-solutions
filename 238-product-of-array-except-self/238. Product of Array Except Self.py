class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        acc1 = 1
        acc2 = 1
        for i,num in enumerate(nums):
            acc1 *= num
            prefix[i] = acc1
        for i in range(len(nums) -1, -1, -1):
            acc2 *= nums[i]
            suffix[i] = acc2

        res = [0] * len(nums)
        res[0] = suffix[1]
        res[-1] = prefix[-2]
        for i in range(1, len(res) - 1):
            res[i] = prefix[i-1] * suffix[i+1]
        return res

        