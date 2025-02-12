class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # (val, idx) 
        # Stack to be monotonically decreasing
        res = [0] * len(temperatures)
        idx = 0
        while idx < len(temperatures):
            while stack and temperatures[idx] > stack[-1][0]:
                val, i = stack.pop()
                # We found a warmer one
                res[i] = idx - i
            stack.append((temperatures[idx], idx))
            idx += 1
        return res