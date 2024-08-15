class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten, twenty = 0, 0, 0
        for i in range(len(bills)):
            if bills[i] == 5:
                five += 1
            elif bills[i] == 10:
                if five > 0:
                    ten += 1
                    five -= 1
                else:
                    return False
            elif bills[i] == 20:
                if five > 0 and ten > 0:
                    ten -= 1
                    five -= 1
                    twenty += 1
                elif five > 2:
                    five -= 3
                    twenty += 1
                else:
                    return False
        return True

        