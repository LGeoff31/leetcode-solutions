class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        a=[]
        for b in s:
            if b.isalpha():
                a.append(b)
        a=a[::-1]
        res = "" 
        idx = 0
        for i in range(len(s)):
            if not s[i].isalpha():
                res += s[i]
            else:
                res += a[idx]
                idx += 1
        return res
        