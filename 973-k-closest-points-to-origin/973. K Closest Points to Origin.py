class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dic = defaultdict(list)
        distances = []
        for x,y in points:
            dic[math.sqrt(x**2 + y**2)].append((x,y))
            distances.append(math.sqrt(x**2 + y**2))
        heapq.heapify(distances)
        res = []
        print(dic)
        z = 0
        while z != k:
            a = heapq.heappop(distances)
            arr = dic[a]
            for x, y in arr:
                res.append([x,y])
                z += 1
                if z == k: break
        return res
        

        