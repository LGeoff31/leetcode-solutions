class Solution:
    def sortVowels(self, s: str) -> str:
        # return "".join(list(reversed(sorted(list(s)))))
        v = []
        a = []
        for c in s:
            if c in {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}:
                v.append(c)
        v.sort()
        res = ""
        idx = 0
        for c in s:
            if c in {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}:
                res += v[idx]
                idx += 1
            else:
                res += c
        return res
        # return "".join(sorted(v)) + "".join(a)