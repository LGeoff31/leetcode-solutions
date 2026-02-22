class Solution:
    def binaryGap(self, n: int) -> int:
        b = bin(n)[2:]
        res = 0
        for i in range(len(b)):
            if b[i] == '1':
                for j in range(i+1, len(b)):
                    if b[j] == '1':
                        res = max(res, j-i)
                        break
        return res
