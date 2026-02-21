class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dfs(i, curr):
            if curr == amount:
                return 1
            if curr > amount or i >= len(coins):
                return 0
            res = 0
            for j in range(0, ceil((amount-curr)/coins[i]) + 1):
                res += dfs(i+1, curr + coins[i] * j)
            return res
        return dfs(0, 0)