class Solution:
    def resultingString(self, s: str) -> str:
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            else:
                if (c == "z" and stack[-1] == "a") or c == "a" and stack[-1] == "z" or abs(ord(c)-ord(stack[-1])) == 1:
                    stack.pop()
                else:
                    stack.append(c)
            # print(stack)

        return "".join(stack)