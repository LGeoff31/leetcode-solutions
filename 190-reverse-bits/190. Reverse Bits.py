class Solution:
    def reverseBits(self, n: int) -> int:
        mask = 1 << 31
        result = 0
        for i in range(32):
            if n & mask:
                result += 2**(i)
            mask >>= 1

        return result
        