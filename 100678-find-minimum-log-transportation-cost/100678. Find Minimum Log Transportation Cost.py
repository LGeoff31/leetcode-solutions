class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        res = 0
        if n > k:
            res += (n-k) * k
        if m > k:
            res += (m-k) * k
        return res