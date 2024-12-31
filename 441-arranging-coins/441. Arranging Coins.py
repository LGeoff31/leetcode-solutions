class Solution:
    def arrangeCoins(self, n: int) -> int:
        #a^2 + a -2n = 0
        a = (-1 + sqrt(1 - 4*1*(-2*n))) / 2
        print(a)
        return floor(a)