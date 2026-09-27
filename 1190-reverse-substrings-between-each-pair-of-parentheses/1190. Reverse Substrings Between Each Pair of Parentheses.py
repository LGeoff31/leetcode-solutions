class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for c in s:
            if c == "(":
                stack.append("(")
            elif c == ")":
                curr = ""
                while stack[-1] != "(":
                    curr += stack.pop()
                stack.pop()
                for c in curr:
                    stack.append(c)
            else:
                stack.append(c)
        return "".join(stack)
            