class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        ones = bin(num2).count("1")
        def convert(bin):
            res = 0
            for i in range(len(bin) - 1, -1, -1):
                if bin[i] == "1":
                    res += 2 ** (32 - (i+1))
            return res
        if ones <= bin(num1).count("1"):
            a = bin(num1)[2:]
            a = "0" * (32 - len(a)) + a
            print(a, ones)
            lst = ["0"] * 32
            for i in range(len(a)):
                if a[i] == "1":
                    lst[i] = "1"
                    ones -= 1
                    num1 -= 2 ** (32 - (i+1))
                if ones == 0: break
            return convert("".join(lst))
        else:
            ones -= bin(num1).count("1")
            a = bin(num1)[2:]
            a = "0" * (32 - len(a)) + a
            lst = ["0"] * 32
            res = 0
            print(a, ones)
            valid = True
            for i in range(len(a) - 1, -1, -1):
                if a[i] == "0" and valid:
                    lst[i] = "1"
                    ones -= 1
                elif a[i] == "1":
                    lst[i] = "1"
                if ones == 0: valid = False
                    # res += 2 ** (32 - (i+1))
            print(lst, 'gay')
            return convert("".join(lst))
