class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        dp = [[0] * k for _ in range(len(nums))]
        dp[0][nums[0] % k] = 1

        for i in range(1, len(nums)):
            val = nums[i] % k
            dp[i][val] += 1
            for r in range(k):
                dp[i][(r*val)%k] += dp[i-1][r]
        
        res = [0] * k
        for r in range(k):
            for i in range(len(nums)):
                res[r] += dp[i][r]
        return res