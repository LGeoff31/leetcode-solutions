class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = 0
        p = 1
        for c in str(n):
            p *= int(c)
            s += int(c)
        return n % (s+p) == 0