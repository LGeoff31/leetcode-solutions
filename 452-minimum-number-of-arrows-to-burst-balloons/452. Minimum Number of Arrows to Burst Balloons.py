class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        print(points)
        idx = 0
        res = 0
        while idx < len(points):
            newIdx = idx+1
            num = points[idx][1]
            while newIdx < len(points):
                if num >= points[newIdx][0]:
                    num = min(num, points[newIdx][1])
                    newIdx+=1
                    if newIdx == len(points): return res+1
                else:
                    idx = newIdx-1
                    break

            idx+=1
            res +=1
        return res

        