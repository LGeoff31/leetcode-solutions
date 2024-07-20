class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows, cols = len(rowSum), len(colSum)
        res = [[0] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                minimum = min(rowSum[r], colSum[c])
                res[r][c] = minimum
                rowSum[r] -= minimum
                colSum[c] -= minimum 
        return res
        