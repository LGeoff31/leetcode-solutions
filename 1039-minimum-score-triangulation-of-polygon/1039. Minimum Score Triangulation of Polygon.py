class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        """
        Triangles are made by 3 sides that fall: adjacent or circular
        """
        n = len(values)
        @cache
        def dfs(start, end):
            if end-start < 2:
                return 0
            res = 1e9
            for k in range(start + 1, end):
                res = min(res, (values[start] * values[end] * values[k]) + dfs(start, k) + dfs(k, end))
            return res
        return dfs(0, n - 1)