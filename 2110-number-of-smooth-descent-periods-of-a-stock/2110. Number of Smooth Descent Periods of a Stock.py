class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        curr = 1
        res = 0
        for i in range(1, len(prices)):
            if prices[i] == prices[i-1] - 1:
                curr += 1
            else:
                res += curr * (curr + 1) // 2
                curr = 1
        if curr > 0:
            res += curr * (curr + 1) // 2
        return res 