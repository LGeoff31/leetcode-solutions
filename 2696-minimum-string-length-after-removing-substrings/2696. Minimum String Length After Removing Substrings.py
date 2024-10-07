class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for i in range(len(s)):
            stack.append(s[i])
            if len(stack) >= 2:
                if stack[-1] == "B" and stack[-2] == "A":
                    stack.pop()
                    stack.pop()
                if len(stack) >= 2:
                    if stack[-1] == "D" and stack[-2] == "C":
                        stack.pop()
                        stack.pop() 
            
        return len(stack)
        