class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        timeSeries.sort()
        stack = []
        for start in timeSeries:
            if not stack:
                stack.append([start, start + duration - 1])
            else:
                lastStart, lastEnd = stack[-1]
                if lastEnd >= start:
                    stack[-1] = [lastStart, max(lastEnd, start + duration - 1)]
                else:
                    stack.append([start, start + duration - 1])
        res = 0
        for start, end in stack:
            res += end - start + 1
        return res