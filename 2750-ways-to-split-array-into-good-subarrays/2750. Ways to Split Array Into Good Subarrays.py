class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        MOD = 10**9+7   
        ones = []
        total = 0
        zeros = 1

        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            else:
                if total == 0:
                    total = 1
                else:
                    total *= zeros % MOD
                zeros=1
        return total % MOD