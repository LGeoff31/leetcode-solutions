class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # The min val must be x
        # For next value, you want to find the next min value such that it contains all 1 bit's of nums[i-1]
        a = "0" * (56-len(bin(x)[2:])) + bin(x)[2:]

        lst = []
        for i, c in enumerate(a):
            if c == "0":
                lst.append(55 - i)
        n -= 1
        lst.sort()
        print(lst)
        a = list(a)
        idx = 0
        print(len(a))
        print(n)
        while n != 0:
            if n%2==1:
                a[55 - lst[idx]] = "1"
            n //= 2
            idx += 1
            if idx >= len(lst): break
        res = 0
        for i in range(len(a) -1, -1, -1):
            if a[i] == "1":
                res += 2 ** (55 - i)
        print(a)
        return res