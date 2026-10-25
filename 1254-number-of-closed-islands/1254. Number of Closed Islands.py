class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        """
    0,0,1,1,0,1,0,0,1,0
    1,1,0,1,1,0,1,1,1,0
    1,0,1,1,1,0,0,1,1,0
    0,1,1,0,0,0,0,1,0,1
    0,0,0,0,0,0,1,1,1,0
    0,1,0,1,0,1,0,1,1,1
    1,0,1,0,1,1,0,0,0,1
    1,1,1,1,1,1,0,0,0,0
    1,1,1,0,0,1,0,1,0,1
    1,1,1,0,1,1,0,1,1,0

        """
        closed_islands = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def is_boundary(r,c):
            return r == 0 or c == 0 or r == rows - 1 or c == cols - 1

        def bfs(r,c):
            queue = deque([(r,c)])
            visited.add((r,c))
            is_enclosed = True

            while queue:
                r,c = queue.popleft()
                if is_boundary(r,c):
                    is_enclosed = False

                for nei_r, nei_c in [(r+1, c), (r-1, c), (r, c+1), (r,c-1)]:
                    if 0 <= nei_r < rows and 0 <= nei_c < cols and grid[nei_r][nei_c] == 0 and (nei_r, nei_c) not in visited:
                        visited.add((nei_r, nei_c))
                        queue.append((nei_r, nei_c))
            
            return is_enclosed

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 and (r,c) not in visited:
                    is_enclosed = bfs(r,c)
                    closed_islands += int(is_enclosed)
            
        return closed_islands
                    