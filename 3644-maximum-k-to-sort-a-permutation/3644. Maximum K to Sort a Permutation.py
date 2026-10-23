class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)

        a = 2 ** 31 -1
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                a &= nums[i]
        return a if a != 2**31 - 1 else 0
