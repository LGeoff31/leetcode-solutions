class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # 1/ 8^k
        queue = deque([(row, column)])
        directions = [(-1, 2), (-1, -2), (1, 2), (1,-2), (2, 1), (2,-1), (-2, 1), (-2, -1)]
        count = 0
        @cache
        def dfs(r,c,k):
            if k == 0:
                return 0 <= r < n and 0 <= c < n
            if not(0 <= r < n and 0 <= c < n):
                return 0
            res = 0
            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc
                res += dfs(new_r, new_c, k-1)
            return res

        return dfs(row, column, k) / (8**k)