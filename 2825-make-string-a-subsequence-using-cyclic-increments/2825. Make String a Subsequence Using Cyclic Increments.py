class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        # ezpzzy greedy algorithm
        a,b = 0, 0
        def valid(a,b):
            return 0<=ord(b)-ord(a)<= 1 or ord(a)-ord(b)==25
        while a < len(str1) and b < len(str2):
            if valid(str1[a], str2[b]):
                a += 1
                b += 1
            else:
                a += 1
        return b == len(str2)
