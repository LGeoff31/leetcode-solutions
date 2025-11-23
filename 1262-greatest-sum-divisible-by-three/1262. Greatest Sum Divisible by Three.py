class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        """
        dp[pos][mod]
        """
        @cache
        def dfs(i, mod):
            if i == len(nums):
                if mod == 0:
                    return 0
                return -1e9

            # TAKE
            # DONT TAKE
            return max(
                nums[i] + dfs(i+1, (mod + nums[i]) % 3),
                dfs(i+1, mod)
            )

        return dfs(0, 0)