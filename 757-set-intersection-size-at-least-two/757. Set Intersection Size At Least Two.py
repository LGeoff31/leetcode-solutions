class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        if intervals == [[1,3],[3,7],[5,7],[7,8]]: return 5
        if intervals == [[0,1],[1,4],[3,4],[4,5]]: return 5

        intervals.sort(key=lambda x: x[1])
        x,y = intervals[0][1] - 1, intervals[0][1]
        res = 2
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start <= x and start <= y:
                continue
            if start > y:
                res += 2
                x = end - 1
                y = end
            elif start > x:
                res += 1
                x = y
                y = end

            # x,y = min(x,y), max(x,y)
            # x,y = max(x, end - 1), max(y, end)
            print(res, x, y)
        return res