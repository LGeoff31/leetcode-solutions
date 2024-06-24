class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        res = 0
        flips = 0

        for i in range(len(nums)):
            if i >= k: # First time shifting window
                flips -= nums[i-k] == 2
            if flips % 2 == nums[i]: # We must toggle
                if i+k-1 >= len(nums):
                    return -1
                nums[i] = 2
                flips += 1
                res += 1
        return res