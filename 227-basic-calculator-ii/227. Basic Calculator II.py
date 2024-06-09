class Solution:
    def calculate(self, s: str) -> int:
        operation = "+"
        currNum = ""
        stack = [] 
        s = s.strip()
        if len(s) == 1 or ("+" not in s and "-" not in s and "*" not in s and "/" not in s):
            return int(s)

        for i, c in enumerate(s):
            if c.isdigit():
                if i == len(s) - 1:
                    currNum += c
                    z = stack.pop()
                    # print("last", stack, z, currNum, operation)
                    if operation == "*":
                        stack.append(int(z) * int(currNum))
                    elif operation == "/":
                        if (int(z) < 0 or int(currNum) < 0) and not (int(z) < 0 and int(currNum) < 0):
                            stack.append( - (abs(int(z)) // abs(int(currNum))))
                        else:
                            stack.append(int(z) // int(currNum))
                    elif operation == "-":
                        stack.append(int(z) - int(currNum))
                    else:
                        stack.append(int(z) + int(currNum))
                else:
                    currNum += c
            elif c in "+-*/":
                if operation == "*":
                    z = stack.pop()
                    stack.append(int(z) * int(currNum))
                elif operation == "/":
                    z = stack.pop()
                    if (int(z) < 0 or int(currNum) < 0) and not (int(z) < 0 and int(currNum) < 0):
                        stack.append( - (abs(int(z)) // abs(int(currNum))))
                    else:
                        stack.append(int(z) // int(currNum))
                    # stack.append(int(z) // int(currNum))
                elif operation == '-':
                    stack.append(-int(currNum))
                else:
                    stack.append(int(currNum))

                currNum = ""
                operation = c
            # print(stack, c)

        return sum([int(num) for num in stack])

