class Solution:
    def findIntegers(self, n: int) -> int:
        f = [1,2]
        for i in range(30):
            f.append(f[-1] + f[-2])
        def get_rid_leading_zeros(expr):
            for i in range(len(expr)):
                if expr[i] == "1":
                    return expr[i:]
        expr =get_rid_leading_zeros(bin(n)[2:])
        prevTwoWasOne = False
        def valid(expr):
            for i in range(1, len(expr)):
                if expr[i] == "1" and expr[i-1] == "1":
                    return 0
            return 1
        res = valid(expr)
        print(res, expr)
        n = len(expr)
        curr = 0
        for i in range(len(expr)):
            if curr == 2: prevTwoWasOne = True
            if expr[i] == "1":
                if not prevTwoWasOne:
                    res += f[n-i-1]
                curr += 1
            else:
                curr = 0
        return res
