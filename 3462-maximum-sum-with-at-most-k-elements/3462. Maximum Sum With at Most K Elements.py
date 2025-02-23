class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        # DP or greedy or HEAP??!?
        lst = []
        for i in range(len(grid)):
            grid[i] = sorted(grid[i], reverse=True)
            for j in range(limits[i]):
                lst.append(grid[i][j])
        lst.sort(reverse=True)
        return sum(lst[:k])