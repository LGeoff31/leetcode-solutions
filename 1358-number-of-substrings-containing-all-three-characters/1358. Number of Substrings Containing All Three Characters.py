class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        dic = defaultdict(int)
        r = 0
        n = len(s)
        for l in range(len(s)):
            while r < len(s) and len(dic) != 3:
                dic[s[r]] += 1
                r += 1
            if len(dic) == 3:
                res += n-r+1
            dic[s[l]] -= 1
            if dic[s[l]] == 0:
                del dic[s[l]]

        return res