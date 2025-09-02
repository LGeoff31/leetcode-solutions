class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        n, m = len(workers), len(bikes)
        @cache
        def dfs(w_mask, b_mask):
            if w_mask == 0:
                return 0
            res = 1e20
            
            for i in range(n):
                if w_mask >> i & 1:
                    for j in range(m):
                        if b_mask >> j & 1:
                            x1,y1 = workers[i]
                            x2,y2 = bikes[j]
                            m_distance = abs(x1-x2) + abs(y1-y2)
                            res = min(res, m_distance + dfs(w_mask & ~(1 << i), b_mask & ~(1 << j)))
                    break
            return res
        return dfs((1 << n) - 1, (1 << m) - 1)