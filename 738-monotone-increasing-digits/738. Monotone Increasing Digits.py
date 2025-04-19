class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        # Edge case: MSB is 1 and 2nd MSB is 0, perhaps change length
        n = str(n)
        # if len(n) >=2 and n[0] == 1 and n[1] == 0 and n
        stack = []
        done = False
        for i in range(len(n)):
            stack.append(n[i])
            while len(stack) > 1 and stack[-1] < stack[-2]:
                stack.pop()
                stack.append(str(int(stack.pop()) - 1))
                done = True
            
            if done: break
        for i in range(len(n) - len(stack)):
            stack.append("9")
        return int("".join(stack))