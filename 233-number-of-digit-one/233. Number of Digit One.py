class Solution:
    def countDigitOne(self, n: int) -> int:
        length = len(str(n))
        res = 0

        for i in range(1, length + 1):
            if i == 1:
                res += (n // (10 ** i) * 10**(i-1)) 
                if n % 10 != 0: res +=1
            else:
                res += (n // (10 ** i) * 10**(i-1)) + min(max(n % (10 ** i) - (10**(i-1)) + 1, 0), 10**(i-1))
            print(res)
        return res