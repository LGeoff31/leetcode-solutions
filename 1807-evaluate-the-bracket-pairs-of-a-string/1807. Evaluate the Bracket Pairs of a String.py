class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # for faster knowledge lookups, make it a hashmap
        know = {}
        for k in knowledge:
            know[k[0]] = k[1]

        # sliding window? can grab indices for substrings
        res = []
        isKey = False
        key_l = 0

        # substrings before first ( ?
        # how to flag after seeing a (

        for i, c in enumerate(s):
            if c == "(":
                isKey = True
                key_l = i + 1
            elif c == ")":
                isKey = False
                key = s[key_l:i]
                if key in know.keys():
                    res.append(know[key])
                else:
                    res.append("?")
            elif isKey == False:
                res.append(c)

        return "".join(res)