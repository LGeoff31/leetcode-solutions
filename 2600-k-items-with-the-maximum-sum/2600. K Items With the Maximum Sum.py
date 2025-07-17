class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        res = min(numOnes, k)
        k -= min(numOnes, k)
        if k == 0:
            return res
        k -= numZeros
        if k <= 0:
            return res
        return res - k