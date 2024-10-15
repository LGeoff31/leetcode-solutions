class Solution:
    def minimumSteps(self, s: str) -> int:
        ones = s.count("1")
        res = 0
        lst = []
        for i in range(len(s) - ones, len(s)):
            if s[i] == "0":
                lst.append(i)
        lst.sort(reverse=True)
        for i in range(len(s) - ones - 1, -1, -1):
            if s[i] == "1":
                res += lst[-1] - i
                lst.pop()
        return res
            
        