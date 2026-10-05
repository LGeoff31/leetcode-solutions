class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        """
        (()()())()
        """
        res = 0
        stack = []

        for c in s:
            if c == "(":
                stack.append("(")
            else:
                # Try clear as much
                curr = 0
                while stack and stack[-1] != "(":
                    curr += stack.pop()
                stack.pop()

                stack.append(2*curr if curr != 0 else 1)

        return sum(stack)