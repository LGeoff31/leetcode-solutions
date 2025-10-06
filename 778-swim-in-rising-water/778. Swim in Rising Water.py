class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def is_possible(val, r, c):
            if grid[0][0] > val: return False
            queue = deque([(r,c)])
            visited = set()
            visited.add((r,c))
            while queue:
                r, c = queue.popleft()
                if r == n-1 and c == n-1:
                    return True
                for nei_r, nei_c in [(r-1, c), (r+1, c), (r, c+1), (r, c-1)]:
                    if 0 <= nei_r < n and 0 <= nei_c < n and (nei_r, nei_c) not in visited and grid[nei_r][nei_c] <= val:
                        visited.add((nei_r, nei_c))
                        queue.append((nei_r, nei_c))
            return False
        res = 1e9
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if is_possible(grid[r][c], 0, 0):
                    res = min(res, grid[r][c])
        return res