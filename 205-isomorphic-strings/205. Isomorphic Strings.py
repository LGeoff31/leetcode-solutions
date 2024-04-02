class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        keys = set()
        for i in range(len(s)):
            if t[i] in keys and s[i] not in dic:
                return False
            if s[i] in dic:
                if dic[s[i]] != t[i]:
                    return False
            keys.add(t[i])
            # if t[i] in dic:
            #     if dic[t[i]] != s[i]:
            #         return False
            # if t[i] in dic:
            #     if dic[t[i]] != s[i]:
            #         return False
            dic[s[i]] = t[i]
            # dic[t[i]] = s[i]
        return True
        