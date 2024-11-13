class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        def increasing(nums):
            for i in range(1, len(nums)):
                if nums[i] <= nums[i-1]:
                    return False
            return True
        for i in range(len(nums) - 2 * k + 1):
            a = nums[i:i+k]
            b = nums[i+k: i+2*k]
            print(a,b)
            if increasing(a) and increasing(b):
                return True
        return False
