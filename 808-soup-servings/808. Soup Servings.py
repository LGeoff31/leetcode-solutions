class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4800:
            return 1
        n = ceil(n/25)
        @cache
        def dfs(a,b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1
            if b <= 0:
                return 0
            # Try 4 cases
            return 0.25 * (dfs(a-4, b) + dfs(a-3, b-1) + dfs(a-2, b-2) + dfs(a-1, b-3))

        return dfs(n, n)