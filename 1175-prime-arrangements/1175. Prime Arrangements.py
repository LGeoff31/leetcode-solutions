class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        """
        prime indicies: 2,3,5,7,11,....
        """
        MOD = 10 ** 9 + 7
        def is_prime(num):
            if num == 1: return False
            if num == 2: return True
            
            for i in range(2, ceil(sqrt(num) + 1)):
                if num % i == 0:
                    return False 
            return True


        primes = []
        for i in range(1, n+1):
            if is_prime(i):
                primes.append(i)
        
        res = 1
        for i in range(len(primes)):
            res *= (i+1)
        print(primes)
        composites = n - len(primes)
        print(primes, composites)
        return (factorial(len(primes)) * factorial(composites)) % MOD