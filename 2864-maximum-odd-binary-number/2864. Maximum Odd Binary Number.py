class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        res = "1" * (s.count("1") - 1)
        res += "0" * (len(s) - (s.count("1")))
        res += "1"
        return res

        