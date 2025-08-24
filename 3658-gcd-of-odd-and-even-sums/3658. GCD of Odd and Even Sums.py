class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        a,b = 0, 0
        for i in range(1, 2*n+1):
            if i % 2 == 1:
                a += i
            else:
                b += i
        return gcd(a,b)