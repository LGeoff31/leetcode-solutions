class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = []
        a,b = set(), set()
        for i in range(len(A)):
            a.add(A[i])
            b.add(B[i])
            res.append(len(a&b))
        return res