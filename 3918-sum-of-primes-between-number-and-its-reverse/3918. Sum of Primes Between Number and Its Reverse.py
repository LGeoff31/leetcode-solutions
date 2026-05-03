class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        """
        639

        936
        loop will only be 1000, checking prime is sqrt(), could be improved via sieve

        """

        r = int(str(n)[::-1])

        def prime(num):
            if num == 1:
                return False
            if num == 2:
                return True
            for i in range(2, ceil(sqrt(num)) + 1):
                if num % i == 0:
                    return False
            return True

        res = 0
        for i in range(min(n, r), max(n, r) + 1):
            if prime(i):
                res += i
        return res