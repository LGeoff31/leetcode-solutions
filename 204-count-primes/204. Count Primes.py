class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0: return 0
        # Sieve
        prime = [True] * (n+1)
        p = 2
        while p**2 < n:
            if prime[p]:
                for i in range(p*p, n+1, p):
                    prime[i] = False
            p += 1
        count = 0
        for i in range(2, len(prime) - 1):
            if prime[i]:
                count += 1
        return count