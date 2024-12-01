class Solution:
    def smallestNumber(self, n: int) -> int:
        def valid(num):
            a = bin(num)[2:]
            return len(a) == a.count("1")
        for i in range(n, 1000000):
            if valid(i):
                return i
        