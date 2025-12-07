class Solution:
    def largestPrime(self, n: int) -> int:
        def find_primes(n):
            if n < 2:
                return []
            is_prime = [True] * (n+1)
            is_prime[0] = False
            is_prime[1] = False

            limit = int(n ** 0.5)
            for p in range(2, limit + 1):
                if is_prime[p]:
                    for multiple in range(p*p, n+1, p):
                        is_prime[multiple] = False
            primes = []
            for i in range(2, n+1):
                if is_prime[i]:
                    primes.append(i)
            return primes 
        primes = find_primes(n)
        primes_set = set(primes)
        curr = 0
        res = 0
        for p in primes:
            curr += p
            if curr > n:
                break
            if curr <= n and curr in primes_set:
                res = curr
        return res
        # prefix = [0] + list(accumulate(primes))
        # primes_set = set(primes)
        
        # for x in primes[::-1]:
        #     seen = set()

        #     for val in prefix:
        #         if val - x in seen:
        #             return x
        #         seen.add(val)
                
        # return 0
                        