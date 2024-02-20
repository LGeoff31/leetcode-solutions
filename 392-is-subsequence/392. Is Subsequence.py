class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l, r = 0, 0
        if not s:
            return True
        while l < len(s) and r < len(t):
            #base case
            if t[r] == s[l]:
                if l == len(s) - 1:
                    return True
                r += 1
                l += 1
            else:
                r += 1
        return False
        