class Solution:
    def highestPeak(self, grid: List[List[int]]) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        queue = deque([])
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    queue.append((r,c))
                    visited.add((r,c))
        grid = [[0] * cols for _ in range(rows)]
        print(queue)
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                for nxt_r, nxt_c in [(r, c-1), (r,c+1), (r+1, c), (r-1,c)]:
                    if 0 <= nxt_r < rows and 0 <= nxt_c < cols and (nxt_r, nxt_c) not in visited:
                        visited.add((nxt_r, nxt_c))
                        
                        grid[nxt_r][nxt_c] = 1 + grid[r][c]
                        queue.append((nxt_r, nxt_c))
            # print(grid, queue)
        return grid

        # [1,2,3]
        # [0,1,2]
        # [1,2,3]
