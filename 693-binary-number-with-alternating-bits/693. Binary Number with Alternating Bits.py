class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        return not(any(bin(n)[2:][i] == bin(n)[2:][i-1] for i in range(1, len(bin(n)[2:]))))