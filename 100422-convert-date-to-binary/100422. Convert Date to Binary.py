class Solution:
    def convertDateToBinary(self, date: str) -> str:
        a = bin(int(date[:4]))
        b = bin(int(date[5:7]))
        c = bin(int(date[8: 10]))
        return str(a)[2:] + "-" + str(b)[2:] + "-" + str(c)[2:]
        