class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        res = 0
        flips = 0
        flipped = [False] * len(nums)

        for i in range(len(nums)):
            if i >= k: # Window shifting has started, can now remove the element at left pointer
                flips -= nums[i-k] == 2
            
            if flips % 2 == nums[i]: # Must flip
                if i+k-1 >= len(nums):
                    return -1
                res += 1
                flips += 1
                nums[i] = 2
                # flipped[i] = True
        return res
