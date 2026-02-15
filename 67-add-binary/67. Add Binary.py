class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def val(bin_str):
            res = 0
            for i in range(len(bin_str)):
                res += 2 ** (len(bin_str) - i - 1) if bin_str[i] == "1" else 0
            return res

        return bin(val(a) + val(b))[2:]