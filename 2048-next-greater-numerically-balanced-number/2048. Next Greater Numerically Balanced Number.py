class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        # We can try size, size+1, ...
        def valid(num):
            n = str(num)
            return all(n.count(c) == int(c) for c in n)
        start = n+1
        while not valid(start):
            start += 1
        return start