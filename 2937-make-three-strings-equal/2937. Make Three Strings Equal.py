class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        if s1[0] != s2[0] or s2[0] != s3[0] or s1[0] != s3[0]: return -1

        idx = 0
        for i in range(min(len(s1), len(s2), len(s3))):
            c = s1[i]
            if s2[i] == c and s3[i] == c:
                idx = i
            else:
                idx = i-1
                break
        idx+=1
        return len(s1) - idx + len(s2) - idx + len(s3) - idx