class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            stack.append(asteroids[i])
            while len(stack) > 1 and stack[-1] < 0 and stack[-2] > 0:
                if abs(stack[-1]) == abs(stack[-2]):
                    stack.pop()
                    stack.pop()
                elif abs(stack[-1]) > abs(stack[-2]):
                    stack.pop(-2)
                else:
                    stack.pop()
        return stack

        