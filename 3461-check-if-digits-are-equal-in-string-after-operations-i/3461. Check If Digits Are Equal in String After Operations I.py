class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            new_s = ""
            for i in range(len(s) - 1):
                new_s += str((int(s[i]) + int(s[i+1])) % 10)
            s = new_s
        return s[0] == s[1]