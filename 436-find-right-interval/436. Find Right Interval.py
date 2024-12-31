class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        dic = {}
        for i in range(len(intervals)):
            dic[tuple(intervals[i])] = i
        intervals.sort()
        c = [a for a,b in intervals]
        res = [0] * len(intervals)
        print(intervals)
        for i in range(len(intervals)):
            idx = dic[tuple(intervals[i])]
            if bisect_left(c, intervals[i][1]) == len(intervals):
                res[idx] = -1
            else:
                res[idx] = dic[tuple(intervals[bisect_left(c, intervals[i][1])])]
        return res

