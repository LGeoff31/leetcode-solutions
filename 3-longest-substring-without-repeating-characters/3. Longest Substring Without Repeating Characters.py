class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        dic = {}
        l,r = 0, 0
        longest = 0
        while r < len(s):
            if s[r] in dic:
                dic[s[r]] += 1
                while dic[s[r]] > 1:
                    dic[s[l]] -= 1
                    l += 1
            else:
                dic[s[r]] = 1 
            r+=1
            longest = max(longest, r-l)
        return longest
            
        