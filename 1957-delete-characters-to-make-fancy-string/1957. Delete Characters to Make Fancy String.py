class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []
        for c in s:
            if len(stack) < 2:
                stack.append(c)
            else:
                if stack[-1] == c and stack[-2] == c:
                    continue
                else:
                    stack.append(c)
        return "".join(stack)