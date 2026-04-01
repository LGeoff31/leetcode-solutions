class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        lst = [[positions[i], i+1, healths[i], directions[i]] for i in range(len(positions))]
        lst.sort()
        stack = []
        print(lst)
        for i in range(len(lst)):
            if not stack:
                stack.append(lst[i])
            else:
                if lst[i][3] == "L":
                    if stack[-1][3] != "R":
                        stack.append(lst[i])
                    else:
                        found = False
                        while stack and stack[-1][3] == "R":
                            if stack[-1][2] == lst[i][2]:
                                stack.pop()
                                found = True
                                break 
                            elif stack[-1][2] > lst[i][2]:
                                stack[-1][2] -= 1
                                found = True
                                break 
                            else:
                                lst[i][2] -= 1
                                stack.pop()
                        if not found:
                            stack.append(lst[i])
                else:
                    stack.append(lst[i])
        if not stack: return []
        stack.sort(key=lambda x: x[1])
        return [x[2] for x in stack]