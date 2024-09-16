class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # 12h = 7200m
        lst = []
        for time in timePoints:
            hour, mins = time.split(":")
            lst.append(int(hour) * 60 + int(mins))
        res = 1e9
        lst.sort()
        for i in range(len(lst)-1):
            res = min(res, abs(lst[i+1] - lst[i]), 1440 - abs(lst[i+1] - lst[i]))

        return min(res, abs(lst[-1] - lst[0]), 1440 - abs(lst[-1] - lst[0]))
        