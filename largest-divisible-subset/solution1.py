class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        dp = [1] * len(nums)
        nums.sort()
        maxLength, maxIndex = 1, 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], 1 + dp[j])
                    if dp[i] > maxLength:
                        maxLength = dp[i]
                        maxIndex = i

        num = nums[maxIndex]
        lst = []
        for i in range(maxIndex, -1, -1):
            if num % nums[i] == 0 and dp[i] == maxLength:
                lst.append(nums[i])
                num = nums[i]
                maxLength -= 1

        return lst
