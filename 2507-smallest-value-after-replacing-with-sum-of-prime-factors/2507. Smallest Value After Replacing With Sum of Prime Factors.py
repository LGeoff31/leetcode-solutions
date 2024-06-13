class Solution:
    def smallestValue(self, n: int) -> int:
        def check_prime(n): #O(n)
            for i in range(2, 1 + math.floor(math.sqrt(n))):
                if n%i==0:
                    return False
            return True
        
        def find_prime(n):
            primes = []
            divide = 2
            while n != 1:
                if n%divide==0:
                    n//=divide
                    primes.append(divide)
                else:
                    divide += 1
            return primes
                
        visited = set()
        while not check_prime(n) and n not in visited:
            visited.add(n)
            n = sum(find_prime(n))
        return n

        