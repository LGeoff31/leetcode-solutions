class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        res = 0
        def calculateSum(a,b):
            res = 0
            queue = deque([(a,b)])
            local_visited = set()
            local_visited.add((a,b))
            while queue:
                r,c = queue.popleft()
                res += grid[r][c]
                for dr, dc in [(r-1, c), (r+1,c), (r, c+1), (r, c-1)]:
                    if 0 <= dr < rows and 0 <= dc < cols and grid[dr][dc] != 0 and (dr, dc) not in local_visited:
                        local_visited.add((dr, dc))
                        queue.append((dr, dc))
            return res
        def markVisited(a,b):
            queue = deque([(a,b)])
            while queue:
                r,c = queue.popleft()
                visited.add((r,c))
                for dr, dc in [(r-1, c), (r+1,c), (r, c+1), (r, c-1)]:
                    if 0 <= dr < rows and 0 <= dc < cols and grid[dr][dc] != 0 and (dr, dc) not in visited:
                        queue.append((dr, dc))
                
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] != 0:
                    res = max(res, calculateSum(r,c))
                    markVisited(r,c)
        return res
