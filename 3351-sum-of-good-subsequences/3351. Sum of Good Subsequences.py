class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        dp_s = [0] * (max(nums) + 2)
        dp_c = [0] * (max(nums) + 2)
        # dp_s[nums[0]] = nums[0]
        # dp_c[nums[0]] = 1
        for num in nums:
            dp_s[num] += num*(1+dp_c[num+1]+dp_c[num-1])  + dp_s[num+1] + dp_s[num-1]
            dp_c[num] += dp_c[num+1] + dp_c[num-1] + 1
        return sum(dp_s) % MOD