class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        dic = Counter(s)
        print(dic)
        maxCount = max(dic.values())
        for key in dic:
            dic[key] = dic[key] - maxCount + 1

        res = ""
        for i in range(len(s) - 1, -1, -1):
            if dic[s[i]] > 0: 
                res+=s[i]
                dic[s[i]] -= 1
        return res[::-1]
        

        