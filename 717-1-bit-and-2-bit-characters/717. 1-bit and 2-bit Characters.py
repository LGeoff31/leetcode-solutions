class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        if len(bits) == 1: return bits[0] == 0
        while i < len(bits):
            i += bits[i] + 1
            if i == len(bits) - 1:
                return True
        return False