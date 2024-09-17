class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        dic = {}
        res = 0

        while r < len(s):
            dic[s[r]] = 1 + dic.get(s[r], 0)
            while dic[s[r]] > 1:
                dic[s[l]] -= 1
                if dic[s[l]] == 0:
                    del dic[s[l]]
                l += 1
            r += 1
            res = max(res, r-l)
        return res

