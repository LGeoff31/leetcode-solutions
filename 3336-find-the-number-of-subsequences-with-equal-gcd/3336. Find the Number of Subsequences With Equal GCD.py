class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7

        @cache
        def dfs(i, a, b):
            if i == len(nums):
                return a == b
            res = 0
            res += dfs(i+1, gcd(a, nums[i]), b)
            res += dfs(i+1, a, gcd(b, nums[i]))
            res += dfs(i+1, a,b)
            return res % MOD


        
        return dfs(0, 0, 0) - 1 # case taking nothing