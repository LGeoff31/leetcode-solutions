class Solution:
    def mostFrequentPrime(self, grid: List[List[int]]) -> int:
        dic = {}
        rows, cols = len(grid), len(grid[0])

        def checkPrime(num):
            for i in range(2, math.ceil(sqrt(num)) + 1):
                if num % i == 0: 
                    return False
            return True
        for r in range(rows):
            for c in range(cols):
                directions_r = (-1, 0, 1)
                directions_c = (-1, 0, 1)
                for d_r in directions_r:
                    for d_c in directions_c:
                        if d_r != 0 or d_c != 0:
                            a = str(grid[r][c])
                            p, d = r, c
                            while 0<=p+d_r<rows and 0<=d+d_c<cols:
                                p+=d_r
                                d+=d_c
                                a+=str(grid[p][d])
                                if checkPrime(int(a)):
                                    dic[int(a)] = 1 + dic.get(int(a), 0)
        res = -1
        freq = -1e9
        print(dic)
        for key in dic:
            if dic[key] > freq:
                freq = dic[key]
        for key in dic:
            if dic[key] == freq:
                res=max(res, key)

        return res



        