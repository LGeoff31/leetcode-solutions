class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        lst = [intervals[0]]
        for start, end in intervals[1:]:
            if lst[-1][1] >= start:
                lst[-1][1] = max(lst[-1][1], end)
            else:
                lst.append([start, end])
        return lst

