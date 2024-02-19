class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        a = 1
        while True:
            if a == n:
                return True
            if a > n:
                return False
            a *= 2
        
        