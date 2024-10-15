class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1: return k
        if n == 2: return k*k

        prevprev, prev = k, k*k
        for i in range(2, n):
            ans = (k-1) * prev + (k-1) * prevprev
            prevprev = prev
            prev = ans
        return ans
