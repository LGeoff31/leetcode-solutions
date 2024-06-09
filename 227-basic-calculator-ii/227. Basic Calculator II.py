class Solution:
    def calculate(self, s: str) -> int: #2-3/2 -> 1
        num, preSign, stack = 0, "+", []
        for c in s+"+":
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in "+-*/":
                if preSign == "+":
                    stack.append(num)
                elif preSign == "-":
                    stack.append(-num)
                elif preSign == "*":
                    stack.append(stack.pop() * num)
                elif preSign == "/":
                    stack.append(math.trunc(stack.pop() / num))
                
                preSign = c
                num = 0
        return sum(stack)