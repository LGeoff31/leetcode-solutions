class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        stack = [meetings[0]]

        for i in range(1, len(meetings)):
            start, end = meetings[i][0], meetings[i][1]
            if start <= stack[-1][1]:
                a,b = stack.pop()
                stack.append([a, max(end, b)])
            else:
                stack.append([start, end])
            print(stack)
        print(stack)
        res = 0
        #start
        res += stack[0][0] - 1
        #end
        res += days - stack[-1][1]

        for i in range(1, len(stack)):
            res += stack[i][0] - stack[i-1][1] - 1

        return res
        