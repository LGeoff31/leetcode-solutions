class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        for i, c in enumerate(s):
            res += (i+1) * (26 - (ord(c) - ord("a")))
        return res