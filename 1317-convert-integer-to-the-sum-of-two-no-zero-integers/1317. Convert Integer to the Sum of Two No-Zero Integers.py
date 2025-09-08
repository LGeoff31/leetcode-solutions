class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a,b = 1, n-1
        while True:
            if str(a).count("0") == 0 and str(b).count("0") == 0:
                return [a,b]
            a += 1
            b -= 1
