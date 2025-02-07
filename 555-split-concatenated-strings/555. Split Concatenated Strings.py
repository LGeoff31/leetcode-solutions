class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:    
        lst = [max(word, word[::-1]) for word in strs]
        res = ""
        for i in range(len(lst)):
            a = "".join(lst[i+1:] + lst[:i])
            for j in range(len(lst[i])):
                res = max(res, lst[i][j:] + a + lst[i][:j])
                res = max(res, lst[i][::-1][j:] + a + lst[i][::-1][:j])
        return res
            