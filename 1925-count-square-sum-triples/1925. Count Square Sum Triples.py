class Solution:
    def countTriples(self, n: int) -> int:
        res = 0

        for a in range(1, n+1):
            for b in range(1, n+1):
                if sqrt(a**2+b**2).is_integer() and sqrt(a**2+b**2) <= n:
                    res += 1
        return res
