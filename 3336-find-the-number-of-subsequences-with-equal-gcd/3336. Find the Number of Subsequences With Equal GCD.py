class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)

        @cache
        def dfs(idx, g1, g2):
            if idx == n:
                return 1 if g1 != 0 and g1 == g2 else 0
            
            res = dfs(idx+1, g1, g2)

            res += dfs(idx+1, gcd(g1, nums[idx]), g2)
            res += dfs(idx+1, g1, gcd(g2, nums[idx]))
            return res
        
        return dfs(0, 0, 0) % MOD
