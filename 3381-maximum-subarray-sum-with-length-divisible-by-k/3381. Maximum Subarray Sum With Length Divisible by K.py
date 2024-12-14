class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:   
        # if k == 1: 
        prefix = list(accumulate(nums))
        dp = [-2000000000000000] * len(nums)
        dp[k-1] = prefix[k-1]
        for i in range(k, len(nums)):
            dp[i] = max(prefix[i] - prefix[i-k], dp[i-k] + (prefix[i] - prefix[i-k]))
        print(dp)
        return max(dp)