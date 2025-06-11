class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n, res = len(s), -10**9
        for a in '01234':
            for b in '01234':
                if a == b: continue
                d = [0]*(n+1)
                pa = [0]*(n+1)
                cb = [0]*(n+1)
                for i, c in enumerate(s, 1):
                    d[i] = d[i-1] + (c == a) - (c == b)
                    pa[i] = pa[i-1] ^ (c == a)
                    cb[i] = cb[i-1] + (c == b)
                lst = [[[] for _ in range(2)] for _ in range(2)]
                pm  = [[[] for _ in range(2)] for _ in range(2)]
                for j in range(k, n+1):
                    i = j - k
                    ai, bi = pa[i], cb[i] & 1
                    if lst[ai][bi]:
                        pm[ai][bi].append(min(pm[ai][bi][-1], d[i]))
                    else:
                        pm[ai][bi].append(d[i])
                    lst[ai][bi].append(cb[i])
                    aj, bj = pa[j], cb[j] & 1
                    na, nb = 1 - aj, bj
                    arr = lst[na][nb]
                    if arr:
                        T = cb[j] - 2
                        h = bisect_right(arr, T) - 1
                        if h >= 0:
                            res = max(res, d[j] - pm[na][nb][h])
        return res