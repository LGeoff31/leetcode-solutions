class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        i = 0
        res = [0] * len(temperatures)
        while i < len(temperatures):
            while stack and stack[-1][1] < temperatures[i]:
                idx, val = stack.pop()
                res[idx] = i - idx
            stack.append((i, temperatures[i]))
            i += 1
        return res
