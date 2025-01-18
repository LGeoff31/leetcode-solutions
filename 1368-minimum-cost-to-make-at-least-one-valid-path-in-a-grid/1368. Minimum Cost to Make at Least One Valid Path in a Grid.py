class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        # 0 <= cost <= rows + cols <= 200
        rows, cols = len(grid), len(grid[0])
        
        queue = deque([(0,0)])
        minCost = [[1e9] * cols for _ in range(rows)]
        minCost[0][0] = 0
        while queue:
            r,c = queue.popleft()
            if r == rows - 1 and c == cols - 1:
                return minCost[r][c]
            for d, dr, dc in [(1, r, c+1), (2,r,c-1), (3,r+1, c), (4, r-1, c)]:
                new_cost = minCost[r][c] + (grid[r][c] != d)
                if 0 <= dr < rows and 0 <= dc < cols and new_cost < minCost[dr][dc]:
                    if d == grid[r][c]:
                        queue.appendleft((dr,dc))
                    else:
                        queue.append((dr, dc))
                    minCost[dr][dc] = new_cost
        print(minCost)
        return -1