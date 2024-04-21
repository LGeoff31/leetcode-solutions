class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[1e9] * cols for _ in range(10)]

        counter = [[0] * cols for _ in range(10)]
        total = 0

        for r in range(rows):
            for c in range(cols):
                counter[grid[r][c]][c]+=1


        for r in range(10):
            for c in range(cols):
                dp[r][c] = rows - counter[r][c]#min changes to make col all have value of r
        for c in range(1, cols):
            for r in range(10):
                temp = 1e9
                for new_r in range(10):
                    if new_r != r:
                        temp = min(temp, dp[new_r][c-1])
                dp[r][c] += temp
        

        res = 1e9
        for r in range(len(dp)):
            res = min(res, dp[r][-1])
        return res


