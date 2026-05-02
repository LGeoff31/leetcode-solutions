class Solution:
    def rotatedDigits(self, n: int) -> int:
        def valid(num):
            a = ""
            for n in str(num):
                if n in ["0", "1", "8"]:
                    a += n
                elif n in ["2", "5"]:
                    a += "2" if n == "5" else "5"
                elif n in ["6", "9"]:
                    a += "9" if n == "6" else "6"
                else:
                    return False
            return str(num) != a
        res = 0
        for i in range(1, n+1):
            res += valid(i)
        return res
                