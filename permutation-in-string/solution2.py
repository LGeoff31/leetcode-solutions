from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lst = []
        s1_dic = Counter(s1)
        for i in range(len(s2) - len(s1) + 1):
            substring = s2[i:i+len(s1)]
            if Counter(substring) == s1_dic:
                return True
        return False
