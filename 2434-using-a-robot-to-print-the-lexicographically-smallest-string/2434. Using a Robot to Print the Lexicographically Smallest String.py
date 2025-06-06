class Solution:
    def robotWithString(self, s: str) -> str:
        suffix = []
        smallest_char = 122
        for i in range(len(s) -1, -1, -1):
            suffix.append(smallest_char)
            smallest_char = min(smallest_char, ord(s[i]))
        suffix = suffix[::-1]
        print(suffix)
        stack = []
        res = ""
        for i in range(len(s)):
            stack.append(s[i])
            # If we have the smallest char on the stack, we can add to res everything from stack
            if stack:
                while stack and ord(stack[-1]) <= suffix[i]:
                    res += stack.pop()

        return res
