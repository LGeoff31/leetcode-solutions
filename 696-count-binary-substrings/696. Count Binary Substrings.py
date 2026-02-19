class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        lst = []
        cnt = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cnt += 1
            else:
                lst.append(cnt)
                cnt = 1
        if cnt >= 1:
            lst.append(cnt)
        
        # [2,2,2,2] -> 3 * 4 // 2
        # [1,1,1,1,1] -> 
        res = 0
        for i in range(1, len(lst)):
            res += min(lst[i], lst[i-1])
            # if lst[i] == lst[i-1]:
                # res += lst[i]
        return res
