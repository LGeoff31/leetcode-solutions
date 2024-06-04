class Solution:
    def longestPalindrome(self, s: str) -> int:
        a = Counter(s)
        res = 0
        odd = False
        if len(a) == 1:
            for key in a:
                return a[key]
        print(a)
        for key in a:
            res += a[key] // 2 * 2
            if a[key]%2 == 0:
                continue
            else:
                odd = True
        print(res)
        return res + odd
            
        