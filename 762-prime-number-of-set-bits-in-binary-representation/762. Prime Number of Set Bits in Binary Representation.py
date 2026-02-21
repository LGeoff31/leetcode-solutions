class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def is_prime(n):
            if n == 1: return False
            if n == 2: return True
            for i in range(2, floor(sqrt(n)) + 1):
                if n % i == 0:
                    return False 
            return True 
        res = 0
        for i in range(left, right + 1):
            if is_prime(bin(i)[2:].count("1")):
                print(bin(i)[2:])
                res += 1
        return res