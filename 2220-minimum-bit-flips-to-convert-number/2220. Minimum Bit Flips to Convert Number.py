class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return str(bin(start ^ goal)).count("1")
        
        # 0000 0101
        # 0000 1000