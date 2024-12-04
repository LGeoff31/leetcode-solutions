class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) != 1:
            num = sum([int(c) for c in str(num)])   
        return num