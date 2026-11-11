class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        goodDeal = costBoth <= cost1 + cost2
        if goodDeal:
            if need1 > need2:
                return min(costBoth * need2 + cost1 * (need1 - need2), costBoth * max(need1, need2))
            return min(costBoth * need1 + cost2 * (need2 - need1), costBoth * max(need1, need2))

        return cost1 * need1 + cost2 * need2