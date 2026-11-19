class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        s, e = intervals[0]
        merged_intervals = [[s, e]]
        for start, end in intervals[1:]:
            if start <= merged_intervals[-1][1]:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], end)
            else:
                merged_intervals.append([start, end])
        return merged_intervals