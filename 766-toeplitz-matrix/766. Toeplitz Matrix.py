class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        def valid(r,c):
            target = matrix[r][c]
            while 0 <= r < rows and 0 <= c < cols:
                if matrix[r][c] != target: 
                    return False
                r += 1
                c += 1
            return True

        rows, cols = len(matrix), len(matrix[0])
        for r in range(rows):
            for c in range(cols):
                if not valid(r,c): return False
        return True