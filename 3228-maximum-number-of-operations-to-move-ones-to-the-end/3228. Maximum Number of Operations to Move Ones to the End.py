class Solution:
    def maxOperations(self, s: str) -> int:
        curr = 0
        i = 0
        res = 0
        while i < len(s):
            if s[i] == "1":
                res += curr
                while i < len(s) and s[i] == "1":
                    curr += 1
                    i += 1
            else:
                i += 1
        if s[-1] == "0":
            res += curr
        return res
            
