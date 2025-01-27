class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        res = 0
        def isSubsequence(s, t):
            t = iter(t)
            return all(c in t for c in s)
            
        for i in range(len(strs)):
            valid = True
            for j in range(len(strs)):
                if i == j: continue
                if isSubsequence(strs[i], strs[j]) == True:
                    valid = False
                    break
            if valid:
                res = max(res, len(strs[i]))
        return res if res > 0 else -1
