class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()

        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1
        k %= 2
        nums.sort()
        if k == 1:
            nums[0] = -nums[0]
        return sum(nums)