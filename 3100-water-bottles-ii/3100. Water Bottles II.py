class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        res = 0
        empty = 0
        while numBottles != 0:
            res += numBottles
            empty += numBottles
            nxt_amount = 0
            while empty >= numExchange:
                empty -= numExchange
                numExchange += 1
                nxt_amount += 1
            numBottles = nxt_amount
        return res 
        
        