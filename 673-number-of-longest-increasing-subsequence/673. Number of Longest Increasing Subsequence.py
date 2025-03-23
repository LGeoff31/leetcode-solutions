class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # Part 1: Find length of LIS
        # Part 2: Find # of LIS of that length
        n = len(nums)
        dp = [1] * n
        count = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if 1 + dp[j] > dp[i]:
                        dp[i] = 1 + dp[j]
                        count[i] = count[j]
                    elif dp[i] == dp[j] + 1:
                        count[i]+= count[j]
        return sum(count[i] for i in range(len(count)) if dp[i] == max(dp))
        print(dp)
        print(count)
        maxLength = max(dp)