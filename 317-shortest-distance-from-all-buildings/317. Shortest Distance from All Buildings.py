class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        buildings = []
        dic = {}
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    buildings.append((r,c))
        
                if grid[r][c] == 0:
                    dic[(r,c)] = [0, 0] # Building visits, Total length
        def bfs(r,c):
            queue = deque([(r,c,0)]) # (r,c,path_length)
            visited = set()
            visited.add((r,c))
            while queue:
                for i in range(len(queue)):
                    r,c,steps = queue.popleft()
                    if grid[r][c] == 0:
                        dic[(r,c)][0] += 1
                        dic[(r,c)][1] += steps

                    for new_r, new_c in [(r-1, c), (r+1,c), (r, c+1), (r,c-1)]:
                        if 0 <= new_r < rows and 0 <= new_c < cols and (new_r, new_c) not in visited and grid[new_r][new_c] == 0:
                            visited.add((new_r, new_c))
                            queue.append((new_r, new_c, steps + 1))
            
        for r,c in buildings:
            # Perform a BFS to touch all 0's and update the dic
            bfs(r,c)
        
        res = 1e9
        for key in dic:
            if dic[key][0] == len(buildings):
                res = min(res, dic[key][1])
        return res if res != 1e9 else -1
