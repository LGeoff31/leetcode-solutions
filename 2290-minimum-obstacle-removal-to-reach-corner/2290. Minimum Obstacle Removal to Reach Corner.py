class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = {}
        adj = defaultdict(list)

        for r in range(rows):
            for c in range(cols):
                # Add up
                if c-1 >= 0:
                    adj[(r,c)].append([r, c-1, grid[r][c-1]])
                # Add right
                if r+1 < rows:
                    adj[(r,c)].append([r+1, c, grid[r+1][c]])
                # Add down
                if c+1 < cols:
                    adj[(r,c)].append([r, c+1, grid[r][c+1]])
                # Add up
                if r-1 >= 0:
                    adj[(r,c)].append([r-1, c, grid[r-1][c]])
        minHeap = [(0, 0, 0)]
        while minHeap:
            w1, r1, c1 = heappop(minHeap)
            if (r1, c1) in visited:
                continue
            visited[(r1, c1)] = w1
            for r2, c2, w2 in adj[(r1, c1)]:
                if (r2, c2) not in visited:
                    heappush(minHeap, (w1+w2, r2, c2))
        # print(visited)
        return visited[(rows-1, cols-1)]