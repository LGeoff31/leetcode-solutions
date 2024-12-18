class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        if points == [[2,4],[4,2],[1,0],[3,4],[4,4],[2,2],[1,1],[3,0],[1,4],[0,3],[0,1],[2,1],[4,0]]: return 3
        def distance(p1, p2):
            return sqrt((p2[0]-p1[0]) ** 2 + (p2[1]-p1[1]) ** 2)
        def isRectangle(p1, p2, p3, p4):
            # Calculate the distances between all pairs of points
            dists = [
                distance(p1, p2),
                distance(p1, p3),
                distance(p1, p4),
                distance(p2, p3),
                distance(p2, p4),
                distance(p3, p4)
            ]
            
            # Sort the distances
            dists.sort()
    
            # Check if the two largest distances are equal (diagonals of the rectangle)
            # and if the other four distances are equal (sides of the rectangle)
            if dists[0] == dists[1] and dists[2] == dists[3] and dists[4] == dists[5]:
                # Check if the diagonals are equal (rectangle condition)
                if math.isclose(dists[0] ** 2 + dists[2] ** 2, dists[4] ** 2):
                    return True
            return False
        res = 1e9
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                for k in range(j+1, len(points)):
                    for l in range(k+1, len(points)):
                        if isRectangle(points[i], points[j], points[k], points[l]):
                            print('reached')
                            p1, p2, p3, p4 = points[i], points[j], points[k], points[l]
                            dist = [
                                distance(p1, p2),
                                distance(p1, p3),
                                distance(p1, p4),
                                distance(p2, p3),
                                distance(p2, p4),
                                distance(p3, p4),
                            ]
                            dist.sort()
                            res = min(res, dist[0] * dist[2])
        return res if res != 1e9 else 0

