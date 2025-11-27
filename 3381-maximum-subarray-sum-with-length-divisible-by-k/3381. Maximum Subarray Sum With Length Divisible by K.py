class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:   
        n = len(nums)
        dp = [-float('inf')] * n
        prefix = list(accumulate(nums))

        for i in range(k-1, len(nums)):
            dp[i] = max((dp[i-k] if i-k>=0 else 0),0) + (prefix[i] - (prefix[i-k] if i-k>=0 else 0))
        print(dp)
        return max(dp)