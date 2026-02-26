class Solution:
    def numSteps(self, s: str) -> int:
        """
        1101 -> 
        1110 
        0111
        1000
        0100
        0010
        0001
        """
        a = int(s, 2)
        cnt = 0
        while a != 1:
            if a & 1:
                a += 1
            else:
                a >>= 1
            cnt += 1
        return cnt