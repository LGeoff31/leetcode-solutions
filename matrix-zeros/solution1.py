class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        zeros_located = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:  # want make all ith row and jth col all zeros
                    zeros_located.add((i, j))
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i, j) in zeros_located:  # want make ith row and jth col all zeros
                    for m in range(cols):
                        matrix[i][m] = 0
                    for l in range(rows):
                        matrix[l][j] = 0
