class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i=1
        stack = [intervals[0]]
        while i < len(intervals):
            while i < len(intervals) and stack[-1][1] >= intervals[i][0]:
                s, e = stack.pop()
                stack.append((s, max(intervals[i][1], e)))
                i += 1
            else:
                if i == len(intervals):break
                stack.append(intervals[i])
            i += 1
        return stack
