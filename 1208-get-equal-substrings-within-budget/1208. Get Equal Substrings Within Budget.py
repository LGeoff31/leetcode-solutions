class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        l,r = 0, 0

        res = 0
        curr_val = 0
        while r < n:
            curr_val += abs(ord(s[r]) - ord(t[r]))
            print(curr_val)
            while curr_val > maxCost and l < n:
                curr_val -= (abs(ord(s[l]) - ord(t[l])))
                l+=1
            res = max(res, r-l+1)
            r+=1
        return res
