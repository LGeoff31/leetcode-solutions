class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def valid(num):
            b = 1
            for n in str(num):
                b *= int(n)
            
            return b % t == 0
        a = n
        while True:
            if valid(a):
                return a
            a += 1