class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        a = set()
        b = set()
        n = len(A)
        res = [0] * n
        res[0] = 1 if A[0] == B[0] else 0
        a.add(A[0])
        b.add(B[0])
        for i in range(1, n):
            res[i] = res[i-1]
            if A[i] == B[i]:
                res[i] += 1
            else:
                if A[i] in b:
                    res[i] += 1
                if B[i] in a:
                    res[i] += 1
            a.add(A[i])
            b.add(B[i])
            print(a, b, A[i], B[i])
        return res
