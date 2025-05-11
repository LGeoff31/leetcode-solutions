class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        # print(zip(*grid))
        h = [sum(arr) for arr in grid]
        prefix_h = list(accumulate(h))
        v = [sum(col) for col in zip(*grid)]
        prefix_v = list(accumulate(v))
        totalSum = sum(grid[i][j] for i in range(len(grid)) for j in range(len(grid[i])))
        return totalSum % 2 == 0 and (totalSum // 2 in prefix_h or totalSum // 2 in prefix_v)