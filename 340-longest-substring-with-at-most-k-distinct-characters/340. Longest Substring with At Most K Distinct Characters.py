class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        l, r = 0, 0
        # Idea: Sliding window, increase the window until k+1 distinct characters are reached, then shrink the window
        dic = {}
        res = 0
        while r < len(s):
            dic[s[r]] = 1 + dic.get(s[r], 0)
            if len(dic) > k:
                # Shrink window until valid
                while len(dic) > k:
                    dic[s[l]] -= 1
                    if dic[s[l]] == 0:
                        del dic[s[l]]
                    l += 1
            else:
                res = max(res, r-l+1)
            r += 1
        return res
