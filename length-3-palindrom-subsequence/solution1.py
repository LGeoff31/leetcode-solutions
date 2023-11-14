class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        dic = {}
        for char in s:
            dic[char] = []
        res = 0
        for i in range(len(s)-2):
            for j in range(i+2, len(s)):
                if s[i] == s[j]:
                    for k in range(i+1, j):
                        if s[k] not in dic[s[i]]:
                            res += 1
                            dic[s[i]].append(s[k])
        print(dic)
        return res
