class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        res = 0
        max_reachable = 0
        coins.sort()
        idx = 0

        while max_reachable < target:
            if idx < len(coins) and coins[idx] <= max_reachable + 1:
                max_reachable += coins[idx]
                idx += 1
            else:
                max_reachable = max_reachable*2 + 1
                res += 1
        return res
            