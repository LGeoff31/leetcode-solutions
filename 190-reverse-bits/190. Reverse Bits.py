class Solution:
    def reverseBits(self, n: int) -> int:
        return int(("0" * (32 - len(bin(n)[2:])) + bin(n)[2:])[::-1], 2)