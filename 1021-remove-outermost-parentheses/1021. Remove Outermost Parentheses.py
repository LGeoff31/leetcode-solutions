class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ""
        stack = []
        curr = ""
        net = 0

        for c in s:
            if c == "(":
                stack.append("(")
                net += 1
            else:
                net -= 1
                if net == 0:
                    res += "".join(stack[1:])
                    stack = []
                else:
                    stack.append(")")

        return res