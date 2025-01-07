class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        characters = s.split("-")
        string = ""
        for c in characters:
            string += c
        idx = 0
        res = ""
        print(string)
        remainder = len(string) % k
        if remainder:
            for i in range(remainder):
                res += string[i].upper()
                idx += 1
            res += "-"
        while idx + k <= len(string):
            a = ""
            for c in string[idx: idx + k]:
                if not c.isdigit() and c.islower():
                    a += c.upper()
                else:
                    a += c
            res += a
            res += "-"
            idx += k

        # a = ""
        # for c in string[idx: idx + k]:
        #     if not c.isdigit() and c.islower():
        #         a += c.upper()
        #     else:
        #         a += c
        # res += a
        return res[:-1]
