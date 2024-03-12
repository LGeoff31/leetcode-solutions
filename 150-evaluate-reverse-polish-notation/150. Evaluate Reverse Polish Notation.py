from math import floor
from math import ceil
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            # print(stack)
            # print(char)
            if char.isdigit() or char[1:].isdigit():
                stack.append(int(char))
            else:
                if char == "+":
                    val = stack[-1] + stack[-2]
                elif char == "-":
                    val = stack[-2] - stack[-1]
                elif char == "*":
                    val = stack[-1] * stack[-2]
                else:
                    val = stack[-2] / stack[-1]
                    if val < 0:
                        val = ceil(val)
                    else:
                        val = floor(val)
                    # print("testing", 6/-132)
                stack.pop()
                stack.pop()
                stack.append(val)
        # print(stack[-1])
        return stack[-1]
        