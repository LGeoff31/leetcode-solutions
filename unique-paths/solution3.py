from collections import deque


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        start_x, start_y = 0, 0
        if m == 1 and n == 1:
            return 1
        memo = {}

        def dfs(start_x, start_y):
            # base case
            # out of bounds
            if start_x > (m-1) or start_y > (n-1):
                return 0
            # end point
            if start_x == (m-1) and start_y == (n-2):  # on the left of end block
                return 1
            if start_x == (m-2) and start_y == (n-1):  # on top of end block
                return 1
            if (start_x, start_y) in memo:
                return memo[(start_x, start_y)]

            memo[(start_x, start_y)] = dfs(start_x + 1,
                                           start_y) + dfs(start_x, start_y + 1)
            return memo[(start_x, start_y)]
        return dfs(0, 0)
