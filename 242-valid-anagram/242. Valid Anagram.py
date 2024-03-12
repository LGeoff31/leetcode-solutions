class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for char in s:
            if t.count(char) == s.count(char):
                continue
            else:
                return False
        return True
        