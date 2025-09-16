class Solution:
    def checkString(self, s: str) -> bool:
        return s[len(s) - s.count("b") : ] == "b" * s.count("b")