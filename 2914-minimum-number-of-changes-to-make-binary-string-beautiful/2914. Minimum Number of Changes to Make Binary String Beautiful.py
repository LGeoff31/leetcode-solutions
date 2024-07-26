class Solution:
    def minChanges(self, s: str) -> int:
        res = 0
        for i in range(0, len(s), 2):
            res += s[i] != s[i+1]
        return res