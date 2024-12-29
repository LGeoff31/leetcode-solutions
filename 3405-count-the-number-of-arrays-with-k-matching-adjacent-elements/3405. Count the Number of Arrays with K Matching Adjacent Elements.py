class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        return (m * (m-1) ** (n-k-1) * comb(n-1, k)) % MOD