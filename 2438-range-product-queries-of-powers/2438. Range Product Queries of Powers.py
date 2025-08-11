class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7
        def get_powers(n):
            start = ceil(log(n, 2)) + 1
            res = []
            while n != 0:
                if 2 ** start <= n:
                    n -= 2 ** start
                    res.append(2 ** start)
                start -= 1
            return list(sorted(res))
        powers = get_powers(n)
        res = []
        for a,b in queries:
            c = 1
            for i in range(a, b+1):
                c *= powers[i]
            res.append(c % MOD)
        return res