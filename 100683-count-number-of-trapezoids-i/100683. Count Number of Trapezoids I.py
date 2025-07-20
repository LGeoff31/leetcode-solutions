class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        """
        How many distinc quadruplets (a,b,c,d) have it that slope(a,b) = slope(c,d) = rise/run = 0
        group points by y-coordinate, 3: [x1, x2, x3... xn] this implies n(n-1)/2 pairs to choose from on yth level
        {0: [1,2,3], 2: [2,3], 3: [1,2,3]} 3 x 1 x 3 = 9
        """
        
        MOD = 10 ** 9 + 7
        dic = defaultdict(list)
        for x,y in points:
            dic[y].append(x)
        print(dic)

        count = 0
        for key in dic:
            if len(dic[key]) > 1:
                count += 1
        if count <= 1:
            return 0
        s = []
        
        for key in dic:
            length = len(dic[key])
            b = length * (length - 1) // 2
            s.append(b)
        c = 0
        for num in s:
            c += num**2
        res = ((sum(s)) ** 2 - c) // 2

        return res % MOD