class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        res = 0
        l = 0
        r = 0

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
                res = max(res, r - l)
            # continue moving l until all unique
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
        
        return res
                