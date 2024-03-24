class Solution:
    def maximumLength(self, s: str) -> int:
        lst = []

        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i:j+1]
                lst.append(substring)

        res = -1
        for substring in lst:
            if lst.count(substring) >= 3 and len(substring) == substring.count(substring[0]):  
                print(substring)
                res = max(res, len(substring))
        return res      