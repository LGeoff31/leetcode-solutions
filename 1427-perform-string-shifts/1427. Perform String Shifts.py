class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        goRight = 0
        for a,b in shift:
            if a == 0:
                goRight -= b
            else:
                goRight += b
        print(goRight)
        goRight %= len(s)
        if goRight >= 0:
            return s[len(s) - goRight:] + s[:len(s) - goRight]
        else:
            return s[abs(goRight) : ] + s[ : abs(goRight)]