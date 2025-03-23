class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        cells = n*n

        able_fill = maxWeight // w

        return min(cells, able_fill)