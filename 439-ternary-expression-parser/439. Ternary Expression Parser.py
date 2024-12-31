# class Ternary:
#     def __init__(self, cond, true_case, false_case):
#         self.cond = cond
#         self.true_case = true_case
#         self.false_case = false_case

class Solution:
    # def parse(self, expr, index):
    #     print(expr, index)
    #     if expr[index:].isnumeric():
    #         return expr, len(expr)
        
    #     condition = expr[index]
    #     index += 2 # skip the T?
    #     true_case, index = self.parse(expr, index)
    #     index += 1 # skip the :
    #     false_case, index = self.parse(expr, index)

    #     return Ternary(condition, true_case, false_case), index

    def parseTernary(self, expression: str) -> str:
        stack = []
        for i, c in enumerate(expression):
            if c == ":":
                idx_last_questionmark = "".join(stack).rfind("?")
                if stack[idx_last_questionmark-1] == "T":
                    # Take everything from after the question mark to the end
                    expr = stack[idx_last_questionmark + 1 : ]
                    # Pop off expr
                    while stack[-1] != "?":
                        stack.pop()
                    stack.pop()
                    stack.pop()
                    for c in expr:
                        stack.append(c)
                else:
                    while stack[-1] != "?":
                        stack.pop()
                    stack.pop()
                    stack.pop()
            else:
                stack.append(c)
        return stack[0]