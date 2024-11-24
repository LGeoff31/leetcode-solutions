class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        smallestNegative = -1e9
        nCount = 0
        totalSum = 0
        zero = False
        smallestNum = 1e9
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                totalSum += abs(matrix[r][c])
                zero = matrix[r][c] == 0 or zero
                if matrix[r][c] < 0:
                    nCount += 1
                    smallestNegative = max(smallestNegative, matrix[r][c])
                if matrix[r][c] > 0:
                    smallestNum = min(smallestNum, matrix[r][c])
        if nCount % 2 == 0 or zero:
            return totalSum
        print(smallestNegative, totalSum)
        if smallestNum < abs(smallestNegative):
            smallestNegative = -smallestNum
        return totalSum + 2 * smallestNegative if smallestNegative != -1e9 else totalSum
                