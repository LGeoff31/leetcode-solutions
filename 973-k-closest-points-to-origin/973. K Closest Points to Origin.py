class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x, y):
            return sqrt(x ** 2 + y ** 2)
        
        max_heap = []

        for x,y in points:
            if len(max_heap) < k:
                heappush_max(max_heap, (dist(x,y), x, y))
            else:
                if dist(x,y) < max_heap[0][0]:
                    heappop_max(max_heap)
                    heappush_max(max_heap, (dist(x,y), x, y))

        return [[b, c] for a,b,c in max_heap] 
        
