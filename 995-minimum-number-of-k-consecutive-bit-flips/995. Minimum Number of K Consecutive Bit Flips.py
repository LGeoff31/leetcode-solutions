class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        res = 0
        flips = 0 # Amount flips within given sliding window
        
        for i in range(len(nums)):
            if i >= k: # Window shifting started
                flips -= nums[i-k] == 2

            if flips % 2 == nums[i]: # You must toggle
                if i+k-1 >= len(nums): #[1,1,0], k=2
                    return -1
                flips += 1
                res += 1
                nums[i] = 2
        return res