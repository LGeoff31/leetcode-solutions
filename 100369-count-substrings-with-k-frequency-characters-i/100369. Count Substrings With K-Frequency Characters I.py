class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        l, r = 0, 0  
        dic = {}  
        n = len(s)
        result = 0

        def valid():
            for count in dic.values():
                if count >= k:
                    return True
            return False

        while r < n:
            dic[s[r]] = dic.get(s[r], 0) + 1

            while valid():
                result += n - r
                dic[s[l]] -= 1
                if dic[s[l]] == 0:
                    del dic[s[l]]
                l += 1
            
            r += 1

        return result
