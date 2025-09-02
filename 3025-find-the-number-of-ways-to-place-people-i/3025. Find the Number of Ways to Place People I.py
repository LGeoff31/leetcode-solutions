class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        def contained(p1, p2, p):
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p
            return min(x1,x2) <= x3 <= max(x1,x2) and min(y1,y2) <= y3 <= max(y1,y2)
        def valid(p1,p2):
            x1, y1 = p1
            x2, y2 = p2
            # Check top left
            if not (x1 <= x2 and y1 >= y2):
                return False
            for i in range(len(points)):
                if points[i] == p1 or points[i] == p2:
                    continue
                if contained(p1, p2, points[i]):
                    return False
            return True
 
        res = 0
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j: continue
                res += valid(points[i], points[j])
        
        return res