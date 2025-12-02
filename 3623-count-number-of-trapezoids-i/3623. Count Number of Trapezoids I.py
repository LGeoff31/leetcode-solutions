class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        dic = defaultdict(int)
        for x,y in points:
            dic[y] += 1
        vals = []
        for key in dic:
            if dic[key] >= 2:
                vals.append(dic[key] * (dic[key] - 1) // 2)
        res = 0
        a=sum(vals) ** 2
        b = 0
        for v in vals:
            b += v ** 2
        return (a - b) // 2 % MOD
        
       

        """

        1, 2, 3, 4, 5

        1x2 + 1x3 + 1x4 + 1x5
        2x3 + 2x4 + 2x5
        3x4 + 3x5
        4x5
        """