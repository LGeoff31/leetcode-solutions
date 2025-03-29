class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        res = s.count("1")
        delta = 0
        i = 0
        leftZeros=0
        while i < len(s):
            ones=0
            while i < len(s) and s[i] == "1":
                ones += 1
                i += 1
            rightZeros = 0
            while i < len(s) and s[i] == "0":
                rightZeros += 1
                i += 1
            if leftZeros and ones and rightZeros:
                delta = max(delta, leftZeros + rightZeros)
            leftZeros = rightZeros
        return res + delta