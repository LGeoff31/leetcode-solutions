class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        lst = []
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(r,c):
            queue = deque([(r,c)])
            visited.add((r,c))
            count = 0
            while queue:
                r,c = queue.popleft()
                count += grid[r][c]
                for new_r, new_c in [(r, c+1), (r,c-1), (r+1, c), (r-1,c)]:
                    if 0 <= new_r < rows and 0 <= new_c < cols and (new_r, new_c) not in visited and grid[new_r][new_c] > 0:
                        visited.add((new_r, new_c))
                        queue.append((new_r, new_c))
            return count
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] > 0:
                    lst.append(bfs(r,c))
        print(lst)
        return sum(num % k == 0 for num in lst)