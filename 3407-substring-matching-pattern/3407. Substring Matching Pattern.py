class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        a,b = p.split("*")
        newString = ""
        if not(a in s and b in s):
            return False
        if not a and b in s or not b and a in s:
            return True
        start1, start2 = -1e9, -1e9
        # Find the start index where a apperas
        for i in range(len(s) - len(a) + 1):
            substring = s[i: i + len(a)]
            if substring == a:
                start1 = i
                break
        for i in range(len(s), len(b), -1):
            substring = s[i - len(b) : i]
            if substring == b:
                start2 = i - len(b)
                break
        print(start1)
        print(start2)
        return start1 + len(a) <= start2
