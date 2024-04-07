class Solution:
    def minimumSteps(self, s: str) -> int:
        res = 0
        zeroCount = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == "1":
                res+=zeroCount
            else:
                zeroCount+=1
        return res
            
        