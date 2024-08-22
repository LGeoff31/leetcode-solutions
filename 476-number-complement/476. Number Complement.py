class Solution:
    def findComplement(self, num: int) -> int:
        a = bin(num)
        print(a[2:])
        res = ""
        for num in a[2:]:
            res += "0" if num == "1" else "1"
        b = 0
        for i in range(len(res) -1, -1, -1):
            b += int(res[i]) * (2 ** (len(res) - i - 1))
        return b
        