class Solution:
    def minScore(self, grid: List[List[int]]) -> List[List[int]]:
        row, col = len(grid), len(grid[0])

        nums = []
        # Create rows and cols to store the minimum values for every row and column.
        rows = [1 for i in range(row)]
        cols = [1 for i in range(col)]

        # Create a matrix nums that stores the values of the matrix and their indices.
        for i in range(row):
            for j in range(col):
                nums.append((grid[i][j], i, j))

        nums.sort()
        for tup in nums:
            _, i, j = tup
            # Find the maximum value of rows[i] and cols[j] till now and assign it to val.
            val = max(rows[i], cols[j])
            grid[i][j] = val
            # Update the new maximum value in rows[i] and cols[j].
            rows[i], cols[j] = val + 1, val + 1
        return grid