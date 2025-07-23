class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pattern(s, first, second, score):
            stack = []
            gain = 0
            for c in s:
                if stack and stack[-1] == first and c == second:
                    stack.pop()
                    gain += score
                else:
                    stack.append(c)
            return "".join(stack), gain
        res = 0
        if x > y:
            s, gain = remove_pattern(s, 'a', 'b', x)
            res += gain
            _, gain = remove_pattern(s, 'b', 'a', y)
            res += gain
        else:
            s, gain = remove_pattern(s, 'b', 'a', y)
            res += gain
            _, gain = remove_pattern(s, 'a', 'b', x)
            res += gain

        return res