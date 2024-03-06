class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        res = len(points)
        if len(points) == 1: return 1
        l, r = 0, 1
        points.sort()   
        print(points)
        prevXMin = points[0][0] #1
        prevXMax = points[0][1] #6
         
        for start, end in points[1:]:
          
            if prevXMin <= start <= prevXMax: 
                res -= 1
                prevXMin = max(prevXMin, start) #2
                prevXMax = min(prevXMax, end) #6
                print(prevXMin, prevXMax)
            else:
                prevXMin = start
                prevXMax = end
                print(prevXMin, prevXMax)


        return res