class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        for i in range(1, n):
            stones[i] += stones[i - 1]
        best = stones[-1]
        for i in range(n - 2, 0, -1):
            best = max(best, stones[i] - best)
        return best