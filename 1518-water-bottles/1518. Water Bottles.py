class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        while numBottles != 0:
            print(res, numBottles)
            res += numBottles // numExchange
            if numBottles // numExchange >= 1:
                numBottles = (numBottles // numExchange) + (numBottles % numExchange)
            else:
                numBottles = 0
        return res
        