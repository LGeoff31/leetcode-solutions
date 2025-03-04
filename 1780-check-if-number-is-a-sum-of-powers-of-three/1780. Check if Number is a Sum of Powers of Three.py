class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        i = floor(log(n, 3))
        while i >= 0:
            if 3 ** i <= n:
                n -= 3 ** i
            i -= 1
        
        return n == 0