class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def distance(p1, p2):
            return sqrt((abs(p2[1] - p1[1]) ** 2) + (abs(p2[0] - p1[0]) ** 2))
        dic = defaultdict(list)
        res = 0
        # O((5 * 10^2) ^ 3) = O(125 * 10 ^ 6) = O(10^8)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dic[distance(points[i], points[j])].append((points[i], points[j]))
        for distance in dic:
            dic2 = defaultdict(int)
            for p1, p2 in dic[distance]:
                dic2[tuple(p1)] += 1
                dic2[tuple(p2)] += 1
            for key in dic2:
                if dic2[key] >= 2:
                    res += 2*( dic2[key] * (dic2[key] - 1) // 2 )
        # print(dic)
        return res