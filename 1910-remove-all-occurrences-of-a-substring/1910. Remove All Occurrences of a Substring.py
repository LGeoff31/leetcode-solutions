class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        def equal(stack):
            if len(stack) < len(part):
                return False
            idx = len(stack) - 1
            idx2 = len(part) - 1
            while idx2 >= 0:
                if stack[idx] != part[idx2]:
                    return False
                idx2 -= 1
                idx -= 1
            return True
        for c in s:
            stack.append(c)
            # print(stack, equal(stack))
            if equal(stack):
                for i in range(len(part)):
                    stack.pop()
        return "".join(stack)