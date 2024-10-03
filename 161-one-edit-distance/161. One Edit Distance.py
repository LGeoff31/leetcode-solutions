class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s==t: return False
        # delete
        def delete(s,t):
            if len(s) != len(t) + 1: return False 
            if not s or not t: return True
            idx1 = 0
            idx2 = 0
            went = False 
            while idx1 < len(s) and idx2 < len(t):
                if s[idx1] != t[idx2]:
                    if went: 
                        return False 
                    else:
                        went = True
                        idx1 += 1
                else:
                    idx1 += 1
                    idx2 += 1
            return True




        # replace
        def replace(s,t):
            diff = 0
            if len(s) != len(t): return False 
            for i in range(len(s)):
                if s[i] != t[i]:
                    diff += 1
            return diff == 1

        return delete(t,s) or delete(s,t) or replace(s,t)