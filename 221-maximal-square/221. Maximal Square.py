class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = deepcopy(matrix)
        for r in range(rows):
            for c in range(cols):
                dp[r][c] = int(dp[r][c])

        for r in range(rows - 2, -1, -1):
            for c in range(cols - 2, -1, -1):
                if matrix[r][c] == "1" and min(dp[r][c+1], dp[r+1][c], dp[r+1][c+1]) >= dp[r][c]:
                    dp[r][c] = min(dp[r][c+1], dp[r+1][c], dp[r+1][c+1]) + 1
        
        return max(dp[r][c] for r in range(rows) for c in range(cols)) ** 2