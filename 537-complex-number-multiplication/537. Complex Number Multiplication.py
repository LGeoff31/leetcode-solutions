class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a,b = num1.split("+")
        a = int(a)
        b = int(b[:-1])  
        c,d = num2.split("+")
        c = int(c)
        d = int(d[:-1])

        real_part = a * c - b * d
        img_part = a * d + b * c
        return f"{real_part}+{img_part}i"