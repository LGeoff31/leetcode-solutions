class Solution:
    def countCommas(self, n: int) -> int:
        res = 0

        for i in range(1, n+1):
            res += (len(str(i))-1) // 3

        return res