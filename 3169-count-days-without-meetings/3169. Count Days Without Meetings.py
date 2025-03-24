class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        stack = []
        meetings.sort()
        for start, end in meetings:
            if not stack:
                stack.append((start, end))
            else:
                if start <= stack[-1][1]:
                    s,e = stack.pop()
                    stack.append((s, max(e, end)))
                else:
                    stack.append((start, end))
        complement_days = 0
        for start, end in stack:
            complement_days += end-start+1
        return days - complement_days