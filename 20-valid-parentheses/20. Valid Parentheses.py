class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == ")":
                if not stack or stack[-1] != "(":
                    return False
                stack.pop()
            elif s[i] == "]":
                if not stack or stack[-1] != "[":
                    return False
                stack.pop()
            elif s[i] == "}":
                if not stack or stack[-1] != "{":
                    return False
                stack.pop()
            else:
                stack.append(s[i])
            

        return not len(stack)