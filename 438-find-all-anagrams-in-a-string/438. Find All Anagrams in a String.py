class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []

        def equal(a, b):
            for key in b:
                if key not in a or b[key] != a[key]: return False
            return True
        b = Counter(p)
        dic = {}

        l = 0
        for r in range(len(s)):
            dic[s[r]] = 1 + dic.get(s[r], 0)
            if r-l+1 < len(p):
                r+=1
            else:
                # print(dic)
                if equal(dic, b):
                    res.append(l)
                r+=1
                dic[s[l]] -= 1
                l += 1
           
        return res