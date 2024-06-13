class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        lst = sentence.split()
        res = []
        for opcode in lst:
            if opcode[0] == "$" and opcode[1:].isdigit():
                num = int(opcode[1:])
                newNum = str(round(num * (1 - discount / 100), 2))
                if len(newNum) - newNum.index(".") - 1 == 1:
                    newNum += "0"
                res.append("$" + newNum)
            else:
                res.append(opcode)
        print(res)
        return " ".join(res)