class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        if len(s) != len(t): return False

        for i in range(len(s)):
            if s[i] in dic:
                if t[i] != dic[s[i]]: return False
            else:
                dic[s[i]] = t[i]
        
        dic = {}
        if len(s) != len(t): return False

        for i in range(len(t)):
            if t[i] in dic:
                if s[i] != dic[t[i]]: return False
            else:
                dic[t[i]] = s[i]
        return True        