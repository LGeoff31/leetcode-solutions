class Solution:
    def maximum69Number (self, num: int) -> int:
        if str(num).count("9") == len(str(num)):
            return num
        a = ""
        b = False
        for c in str(num):
            if c == "6" and not b:
                a += "9"
                b = True
            else:
                a += c
        return int(a)