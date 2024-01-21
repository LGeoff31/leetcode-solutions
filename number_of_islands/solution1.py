from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()

        def bfs(row, col):
            queue = deque([[row, col]])
            while queue:
                for i in range(len(queue)):
                    r, c = queue.popleft()
                    if c+1 < len(grid[0]) and grid[r][c+1] == "1" and (r, c+1) not in visited:
                        queue.append([r, c+1])
                        visited.add((r, c+1))
                    if r+1 < len(grid) and grid[r+1][c] == "1" and (r+1, c) not in visited:
                        queue.append([r+1, c])
                        visited.add((r+1, c))
                    if 0 <= c-1 < len(grid[0]) and grid[r][c-1] == "1" and (r, c-1) not in visited:
                        queue.append([r, c-1])
                        visited.add((r, c-1))
                    if 0 <= r-1 < len(grid) and grid[r-1][c] == "1" and (r-1, c) not in visited:
                        queue.append([r-1, c])
                        visited.add((r-1, c))

        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == "1" and (row, column) not in visited:
                    islands += 1
                    visited.add((row, column))
                    bfs(row, column)
        return islands
