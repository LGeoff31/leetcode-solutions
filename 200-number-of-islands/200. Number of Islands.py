class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0
        visited = set()

        def bfs(r,c):
            queue = deque([(r,c)])
            visited.add((r,c))
            while queue:
                for i in range(len(queue)):
                    r, c = queue.popleft()
                    for new_r, new_c in [(r-1, c), (r+1, c), (r, c+1), (r,c-1)]:
                        if (new_r, new_c) not in visited and 0<=new_r<rows and 0<=new_c<cols and grid[new_r][new_c] == "1":
                            visited.add((new_r, new_c))
                            queue.append((new_r, new_c))
            
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == "1":
                    bfs(r,c)
                    count += 1
        return count