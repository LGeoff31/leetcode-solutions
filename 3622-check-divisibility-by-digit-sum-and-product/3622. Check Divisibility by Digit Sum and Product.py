class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digitSum = sum(int(a) for a in str(n))
        b = 1
        for c in str(n):
            b *= int(c)
        
        return n % (b + digitSum) == 0