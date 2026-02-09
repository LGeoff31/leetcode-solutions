class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def val(bin_str):
            res = 0
            for i in range(len(bin_str)):
                if bin_str[i] == "1":
                    res += 2 ** (len(bin_str) - i - 1)
            return res
        print(val(a))
        print(val(b))

        return bin(val(a) + val(b))[2:]