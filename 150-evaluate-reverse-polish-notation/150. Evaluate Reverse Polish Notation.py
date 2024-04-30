class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ["+", "-", "/", "*"]

        for i in tokens:
            if i in operations:
                a = int(stack.pop())
                b = int(stack.pop())
                if i == "+": stack.append(a+b)
                elif i == "-": stack.append(b-a)
                elif i == "*": stack.append(a*b)
                else: stack.append(b/a)
            else:
                stack.append(i)
        return int(stack[0])

        