class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        # We want either 2 or 4+ divisors
        def is_prime(n):
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True
        # Find numbers which have 3 divisors in range l to r -> squares of prime numbers
        res = 0
        for i in range(math.floor(math.sqrt(l)) - 10, math.floor(math.sqrt(r)) + 10):
            if is_prime(i) and l <= i**2 <= r:
                res += 1
        return r-l+1-res