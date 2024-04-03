class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        #unsigned -> 32 bits
        mask = 1
        for i in range(32):
            if n & mask:
                count += 1
            mask <<= 1
        return count
        