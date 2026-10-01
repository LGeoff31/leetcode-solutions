class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if c == ")":
                    if not stack or stack[-1]!="(": return False
                elif c == "]":
                    if not stack or stack[-1]!="[": return False
                elif c == "}":
                    if not stack or stack[-1]!="{": return False
                stack.pop()
        return len(stack) == 0
