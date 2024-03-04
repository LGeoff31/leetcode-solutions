class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        mask = 1 
        count = 0

        for i in range(32):
            if c & mask:
                if not a & mask and not b & mask: count += 1
            else:
                if a & mask: count += 1
                if b & mask: count += 1
            mask <<= 1
        return count

        