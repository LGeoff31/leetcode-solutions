class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # using costBoth
        option_one = costBoth * min(need1, need2)
        if need1 > need2:
            option_one += (need1-need2) * cost1
        else:
            option_one += (need2-need1) * cost2

        # using cost1 and cost2
        option_two = cost1 * need1 + cost2 * need2

        option_three = costBoth * max(need1, need2)

        return min(option_one, option_two, option_three)

