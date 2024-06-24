class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        res = 0
        flips = 0 # Number of flips within current window
        flipped = [False] * len(nums) #ith element will be flipped -> True

        for i in range(len(nums)):
            if i >= k: # Window shifting
                flips -= flipped[i-k] == True

            if flips % 2 == nums[i]: # You must toggle
                if i+k-1 >= len(nums): #[1,1,0], k=2
                    return -1
                flips += 1
                res += 1
                flipped[i] = True


        return res