class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        total_valid_islands = 0

        def bfs(r,c):
            queue = deque([(r,c)])
            visited.add((r,c))
            total_sum = 0

            while queue:
                r,c = queue.popleft()
                total_sum += grid[r][c]

                for nei_r, nei_c in [(r-1,c),(r+1,c),(r,c+1),(r,c-1)]:
                    if 0 <= nei_r < rows and 0 <= nei_c < cols and (nei_r, nei_c) not in visited and grid[nei_r][nei_c] > 0:
                        visited.add((nei_r, nei_c))
                        queue.append((nei_r, nei_c))

            return total_sum

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0 and (r, c) not in visited:
                    total_sum = bfs(r,c)

                    if total_sum % k == 0:
                        total_valid_islands += 1
        return total_valid_islands