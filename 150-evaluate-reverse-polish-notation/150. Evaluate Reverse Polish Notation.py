class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"+", "-", "*", "/"}

        def perform_calculation(a,b,token):
            if token == "+":
                return a + b
            if token == "-":
                return a-b
            if token == "*":
                return a * b
            if token == "/":
                if a/b < 0:
                    return ceil(a/b)
                return a//b

        for token in tokens:
            if token in operations:
                b,a = stack.pop(), stack.pop()
                stack.append(perform_calculation(a,b,token))
            else:
                stack.append(int(token))
        return stack[0]