class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        initial = 1000

        dic = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100:"C", 90:"XC", 50: "L", 40:"XL", 10: "X", 9:"IX", 5:"V", 4:"IV", 1:"I"}
        if num in dic: return dic[num]
        while num != 0:
            while num >= initial:
                num -= initial
                res += dic[initial]
            if initial == 1000: initial = 900
            elif initial == 900: initial = 500
            elif initial == 500: initial = 400
            elif initial == 400: initial = 100
            elif initial == 100: initial = 90
            elif initial == 90: initial = 50
            elif initial == 50: initial = 40
            elif initial == 40: initial = 10
            elif initial == 10: initial = 9
            elif initial == 9: initial = 5

            elif initial == 5: initial = 4
            elif initial == 4: initial = 1
        return res






        