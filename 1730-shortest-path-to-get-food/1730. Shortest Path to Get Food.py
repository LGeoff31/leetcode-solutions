class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        # * -> start
        # -> food
        rows, cols = len(grid), len(grid[0])
        start_r, start_c = -1, -1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "*":
                    start_r, start_c = r,c
        queue = deque([[start_r, start_c]])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        visited = set()
        visited.add((start_r, start_c))
        chomps = 0
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                if grid[r][c] == "#": return chomps
                for dr, dc in directions:
                    if 0 <= r + dr < rows and 0 <= c + dc < cols and (r+dr, c+dc) not in visited and grid[r+dr][c+dc] != "X":
                        visited.add((r+dr, c+dc))
                        queue.append([r+dr, c+dc])
            chomps += 1
            print(queue)
        return -1