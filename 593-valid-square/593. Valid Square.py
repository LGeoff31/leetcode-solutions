class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if p1 in [p2, p3, p4] or p2 in [p3, p4] or p3 == p4:
            return False
        points = [p1, p2, p3, p4]
        def dist(x1, y1, x2, y2):
            return math.sqrt(abs(y2 - y1) ** 2 + abs(x2 - x1) ** 2)
        
        def closest_points(x1, y1):
            distances = []
            for x,y in points:
                if x1 == x and y1 == y:
                    continue
                distances.append(dist(x1,y1, x, y))
            #there should be two distances that are identical and one that is LARGER
            if not distances: return False, 0, 0
            return len(set(distances)) == 2, max(distances), min(distances)
        
        for x,y in points:
            valid, max_dist, min_dist = closest_points(x,y)
            if not valid:
                return False
        print(max_dist, min_dist)
        if round(min_dist, 10) != round(max_dist / math.sqrt(2), 10):
            return False
        return True
                
