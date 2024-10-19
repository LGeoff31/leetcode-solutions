class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(num):
            b= num
            res = ""
            for c in b:
                if c == "0":
                    res += "1"
                else:
                    res += "0"
            return res
        start = "0"
        def update(string):
            return string + "1" + invert(string)[::-1]
        for i in range(n-1):
            start = update(start)
        return start[k-1]