class Solution:
    def findMismatchedSegments(self, s1: str, s2: str) -> list[list[str]]:
        curr_s1 = ""
        curr_s2 = ""

        res = []

        for i in range(len(s1)):
            if s1[i] == s2[i]:
                if curr_s1:
                    res.append([curr_s1, curr_s2])
                    curr_s1 = ""
                    curr_s2 = ""
            else:
                curr_s1 += s1[i]
                curr_s2 += s2[i]
                
        if curr_s1:
            res.append([curr_s1, curr_s2])
        return res