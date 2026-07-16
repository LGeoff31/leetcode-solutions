class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefixGcd = [0] * n 
        mx = 0

        for i in range(len(nums)):
            mx = max(nums[i], mx)
            prefixGcd[i] = gcd(nums[i], mx)
        
        res = 0
        prefixGcd.sort()
        for i in range(n//2):
            res += gcd(prefixGcd[i], prefixGcd[n-i-1])
        return res