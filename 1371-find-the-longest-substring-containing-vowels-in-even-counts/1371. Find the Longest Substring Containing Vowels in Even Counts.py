class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        dic = {0: -1}
        res = 0
        curr = 0 #00000 -> aeiou

        for i in range(len(s)):
            if s[i] == "a":
                curr = curr ^ (1 << 4)
            if s[i] == "e":
                curr = curr ^ (1 << 3)
            if s[i] == "i":
                curr = curr ^ (1 << 2)
            if s[i] == "o":
                curr = curr ^ (1 << 1)
            if s[i] == "u":
                curr = curr ^ (1 << 0)
            
            if curr in dic:
                res = max(res, i - dic[curr])
                # print(i, curr, res)
            else:
                dic[curr] = i
            # print(dic)
            # print(curr)
        return res



        