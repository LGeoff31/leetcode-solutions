class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        intervals = []
        prev_start = 0

        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                intervals.append([prev_start, i-1])
                prev_start = i
        intervals.append([prev_start, len(s) - 1])

        return [interval for interval in intervals if interval[1] - interval[0] >= 2]
