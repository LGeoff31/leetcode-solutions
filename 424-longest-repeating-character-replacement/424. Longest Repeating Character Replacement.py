class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def works(length):
            dic = {}
            l, r = 0, length - 1
            for i in range(l, r+1):
                dic[s[i]] = 1 + dic.get(s[i], 0)
            # print(dic, length)
            while r < len(s):
                # print(dic)
                if length - max(dic.values()) <= k:
                    return True
                
                r+=1
                if r == len(s): break
                dic[s[r]] = 1 + dic.get(s[r], 0)
                dic[s[l]] -= 1
                if dic[s[l]] == 0:
                    del dic[s[l]]
                l+=1
            
            return False
        
        l, r = 1, len(s)
        res = 0
        while l <= r:
            mid = (l+r) // 2
            if works(mid):
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res


            
        