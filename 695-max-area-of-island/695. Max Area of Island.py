class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if rows * cols == 1:
            return grid[0][0]
        visited = set()
        res = 0
        def bfs(r,c):
            queue = deque([(r,c)])
            count = 1
            while queue:    
                r, c = queue.popleft()
                for nei_r, nei_c in [(r-1,c),(r+1,c),(r,c+1), (r,c-1)]:
                    if 0<=nei_r<rows and 0<=nei_c<cols and grid[nei_r][nei_c] == 1 and (nei_r, nei_c) not in visited:
                        visited.add((nei_r, nei_c))
                        count += 1
                        queue.append((nei_r, nei_c))
            return count

        for r in range(rows):
            for c in range(cols):
                if (r,c) in visited:
                    continue
                    
                visited.add((r,c))
                if grid[r][c] == 1:
                    res = max(res, bfs(r,c))
        return res