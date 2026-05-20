class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = []
        cnt = 0
        a,b = set(), set()
        for i in range(len(A)):
            if A[i] == B[i]:
                cnt += 1
            if A[i] in b:
                cnt += 1
            if B[i] in a:
                cnt += 1
                
            a.add(A[i])
            b.add(B[i])
            res.append(cnt)
        return res