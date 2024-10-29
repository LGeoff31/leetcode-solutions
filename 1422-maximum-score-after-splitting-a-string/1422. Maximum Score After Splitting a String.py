class Solution:
    def maxScore(self, s: str) -> int:
        a,b = s.count("0"), s.count("1")
        zeros, ones = 0, 0
        res = 0
        for i in range(len(s) - 1):
            if s[i] == "0":
                zeros += 1
            else:
                b -= 1
            res = max(res, zeros + b)
        return res

        