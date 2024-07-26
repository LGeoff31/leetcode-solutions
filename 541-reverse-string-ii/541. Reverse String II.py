class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = ""
        i = 0
        n = len(s)
        while i < len(s):
            if n-i < k:
                res += s[i:][::-1]
            elif k <= n-i < 2*k:
                res += s[i: i+k][::-1] + s[i+k:]
            else:
                res += s[i:i+k][::-1] + s[i+k: i+2*k]
            i += 2*k
        return res
