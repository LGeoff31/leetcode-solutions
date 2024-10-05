class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic = {}
        a = Counter(s1)
        if len(s1) > len(s2): return False

        def match():
            for key in dic:
                if key not in a:
                    return False 
                if a[key] != dic[key]:
                    return False 
            return True
        

        l, r = 0, len(s1) - 1
        for i in range(len(s1)-1):
            dic[s2[i]] = 1 + dic.get(s2[i], 0)
        
        while r < len(s2):
            dic[s2[r]] = 1 + dic.get(s2[r], 0)
            if match():
                return True
            dic[s2[l]] -= 1
            if dic[s2[l]] == 0:
                del dic[s2[l]]

            r += 1
            l += 1
        return False