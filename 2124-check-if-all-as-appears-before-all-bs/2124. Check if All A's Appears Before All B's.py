class Solution:
    def checkString(self, s: str) -> bool:
        if "b" not in s or "a" not in s:
            return True
        
        return s.rindex("a") < s.index("b")