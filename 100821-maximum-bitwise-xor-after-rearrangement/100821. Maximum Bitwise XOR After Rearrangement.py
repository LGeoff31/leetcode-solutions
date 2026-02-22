class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        """
        101
        011
        110 -> 6

        0110
        1011
        1101

        0101
        1010
        
        """
        t_counter = Counter(t)
        res = ""
        for c in s:
            if c == "1":
                if t_counter["0"] > 0:
                    res += "0"
                    t_counter["0"] -= 1
                else:
                    res += "1"
                    t_counter["1"] -= 1
            else:
                if t_counter["1"] > 0:
                    res += "1"
                    t_counter["1"] -= 1
                else:
                    res += "0"
                    t_counter["0"] -= 1
        def xor_string(a,b):
            res = []
            for i in range(len(a)):
                res.append('1' if a[i] != b[i] else '0')
            return "".join(res)
        return xor_string(s, res)