class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        i = 0
        prev = 0
        res = 0
        while i < len(brackets) and income > 0:
            amount, percentage = brackets[i]
            net_amount = amount - prev
            if net_amount >= income:
                res += income * percentage / 100
                income = 0
            else:
                res += net_amount * percentage / 100
                prev = amount
                income -= net_amount
            i += 1
        return res