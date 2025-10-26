class Solution:
    def removeZeros(self, n: int) -> int:
        res = ""
        for c in str(n):
            if c != "0":
                res += c

        return int(res)