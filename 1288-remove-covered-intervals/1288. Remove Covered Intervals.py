class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        res = 0     
        def covers(int1, int2):
            return int1[0] <= int2[0] and int2[1] <= int1[1]
            
        for i in range(len(intervals)):
            for j in range(len(intervals)):
                if i == j:
                    continue
                overlap = False
                if covers(intervals[j], intervals[i]):
                    break
            else:
                res += 1
        return res