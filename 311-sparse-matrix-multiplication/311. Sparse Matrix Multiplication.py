class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, k, n = len(mat1), len(mat1[0]), len(mat2[0])

        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                curr = 0
                for z in range(k):
                    curr += mat1[i][z] * mat2[z][j]

                res[i][j] = curr
        return res