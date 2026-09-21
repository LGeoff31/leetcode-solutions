class Solution:
    def calculateTax(self, brackets: list[list[int]], income: int) -> float:
        brackets.sort()

        total = 0
        prev = 0
        for upper_bracket, percent in brackets:
            if income >= upper_bracket:
                total += (upper_bracket - prev) * percent/100
                prev = upper_bracket
            else:
                diff = income - prev
                print('diff', diff, percent, total, )
                total += diff * (percent / 100)
                break
            print(total)
            

        return total