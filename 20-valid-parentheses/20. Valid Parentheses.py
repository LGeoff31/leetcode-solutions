class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) == 1:
            return False
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(s[i])
                continue
            if s[i] == "{":
                stack.append(s[i])
                continue
            if s[i] == "[":
                stack.append(s[i])
                continue
            if s[i] in ")]}" and not stack:
                return False
            if stack:
                if s[i] == ")" and stack[-1] == "(":
                    stack.pop()
                    continue
                elif s[i] == ")":
                    return False
                if s[i] == "]" and stack[-1] == "[":
                    stack.pop()
                    continue
                elif s[i] == "]":
                    return False
                if s[i] == "}" and stack[-1] == "{":
                    stack.pop()
                    continue
                elif s[i] == "}":
                    return False
            print(stack)
            
           
        return not len(stack)
            
        