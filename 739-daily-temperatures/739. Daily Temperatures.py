class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # similar to next greater elem I ?
        # decreasing stack of temps
        # GL HINT: Store tuples in stack

        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while len(stack) >= 1 and t > stack[-1][1]:
                x = stack.pop()
                res[x[0]] = i - x[0]
                # print('pop', x)
            else:
                stack.append((i, t))
                # print(stack)

        return res