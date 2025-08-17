class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        for l, r, k, v in queries:
            while l <= r:
                nums[l] = (nums[l] * v) % MOD
                l += k
        res = 0
        for x in nums:
            res ^= x
        return res
            