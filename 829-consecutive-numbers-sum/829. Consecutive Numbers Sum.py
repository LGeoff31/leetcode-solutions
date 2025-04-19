class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        res = 0
        factors = set()
        for i in range(1, int(sqrt(2*n)) + 1):
            if 2*n % i == 0:
                factors.add(i)
                factors.add(2*n//i)
        for key in factors:
            other_factor = 2*n // key
            z = other_factor + 1 - key
            if z > 0 and z % 2 == 0:
                res += 1
        return res