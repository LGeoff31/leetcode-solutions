class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        a = n
        while True:
            p = [int(p) for p in str(a)]
            b = 1
            print(p)
            for n in p:
                b *= n
            if b % t == 0:
                return a
            a += 1
        