class Solution:
    def totalMoney(self, n: int) -> int:
        res = 0
        base = 1
        while n // 7 > 0:
            z = base + 6
            res += z*(z+1)//2 - (base-1) * base // 2
            base += 1
            n -= 7
        print(res)
        return res + (base + n - 1) * (base + n) // 2 - (base-1)*(base) // 2
