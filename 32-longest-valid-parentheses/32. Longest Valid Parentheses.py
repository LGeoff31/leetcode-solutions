class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """

        )()()(()())))()

        At each index, we can either TAKE / START NEW

        Note if we start new, we should 
        """
        res = 0
        stack = [-1]

        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])

        return res