class Solution:
    def countCollisions(self, directions: str) -> int:
        res = 0 
        stack = []
        for d in directions:
            if d == "L":
                if stack and stack[-1] == "R":
                    res += 2
                    stack.pop()
                    while stack and stack[-1] == "R":
                        res += 1
                        stack.pop()
                    stack.append("S")

                elif stack and stack[-1] == "S":
                    res += 1
            elif d == "R":
                stack.append(d)
            else:
                if stack and stack[-1] == "R":
                    while stack and stack[-1] == "R":
                        res += 1
                        stack.pop()
                stack.append(d)
        return res