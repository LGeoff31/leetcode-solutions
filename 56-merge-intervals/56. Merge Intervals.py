class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = []
        intervals.sort()
        for start, end in intervals:
            if len(stack) == 0:
                stack.append([start, end])
                continue
            if stack[-1][1] >= start:
                prevStart, prevEnd = stack.pop()
                stack.append([min(prevStart, start), max(prevEnd, end)])
            else:
                stack.append([start, end])
        return stack
