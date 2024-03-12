class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        a = {}
        b = {}
        for i in range(len(s)):
            a[s[i]] = 1 + a.get(s[i], 0)
            b[t[i]] = 1 + b.get(t[i], 0)
        if a==b:
            return True
        return False
