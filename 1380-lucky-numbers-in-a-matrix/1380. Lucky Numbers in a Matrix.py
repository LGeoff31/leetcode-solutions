class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rows = []
        cols = []
        row, col = len(matrix), len(matrix[0])

        for r in range(row):
            minElem = 1e9
            for c in range(col):
                minElem = min(minElem, matrix[r][c])
            rows.append(minElem)

        for c in range(col):
            maxElem = -1e9
            for r in range(row):
                maxElem = max(maxElem, matrix[r][c])
            cols.append(maxElem)
        
        res = []
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == rows[r] and matrix[r][c] == cols[c]:
                    res.append(matrix[r][c])
        return res
        