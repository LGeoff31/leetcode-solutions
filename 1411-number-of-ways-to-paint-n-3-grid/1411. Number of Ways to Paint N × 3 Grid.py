class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7

        same = 6  # ABA
        diff = 6  # ABC

        for _ in range(n - 1):
            same_next = (same * 3 + diff * 2) % MOD
            diff_next = (same * 2 + diff * 2) % MOD
            same, diff = same_next, diff_next

        return (same + diff) % MOD