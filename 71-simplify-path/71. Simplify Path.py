class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        a = path.split('/')

        for each in a:
            if each == "..":
                if stack: stack.pop()
            elif each == "." or each=="":
                continue
            else:
                stack.append(each)
        return "/" + "/".join(stack)
        