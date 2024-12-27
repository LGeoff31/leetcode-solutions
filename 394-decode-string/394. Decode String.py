class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i, c in enumerate(s):
            if c == "]":
                string = ""
                while stack[-1] != "[":
                    string += stack.pop()[::-1]
                string = string[::-1]
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    # print(stack[-1])
                    num += stack.pop()
                num = int(num[::-1])
                # print(string, num)
                for i in range(num):
                    stack.append(string)
            else:
                stack.append(c)
            print(stack)
        return "".join(stack)
                