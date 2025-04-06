class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [[num] for num in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if len(dp[j]) >= len(dp[i]):
                        dp[i] = dp[j] + [nums[i]]

        print(dp)

        res = []
        for arr in dp:
            if len(arr) > len(res):
                res = arr

        return res