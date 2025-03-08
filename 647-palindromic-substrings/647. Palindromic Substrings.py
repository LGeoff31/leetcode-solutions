class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        #test odd length
        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
    
        #test even length
        for i in range(len(s) - 1):
            left,right = i, i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1

        return res
        