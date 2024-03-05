class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) - 1
        res = len(s)
        while l < r:
            if s[l:r+1].count(s[0]) == r-l+1: return 0
            while s[l] == s[l+1] and s[r]==s[l]:
                l += 1
            while s[r] == s[r-1] and s[l] == s[r]:
                r -= 1
            if s[l] != s[r]: 
                break
            l += 1
            r -= 1
            if l > r: return 0
        return r-l+1
        