class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # Determine all the islands in grid2 and store them in lst

        lst = []
        visited = set()
        rows, cols = len(grid1), len(grid1[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def bfs(r,c):
            res = [[r,c]]
            queue = deque([[r,c]])
            visited = set()
            visited.add((r,c))
            while queue:
                for i in range(len(queue)):
                    r1, c1 = queue.popleft()
                    for r2, c2 in directions:
                        if 0<=r1+r2<rows and 0<=c1+c2<cols and (r1+r2, c1+c2) not in visited and grid2[r1+r2][c1+c2] == 1:
                            visited.add((r1+r2, c1+c2))
                            res.append([r1+r2, c1+c2])
                            queue.append([r1+r2, c1+c2])
            return res

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid2[r][c] == 1:
                    z = bfs(r,c)
                    lst.append(z)
                    for r3, c3 in z:
                        visited.add((r3, c3))
        print('lst', lst)
        count = 0
        for arr in lst:
            valid = True
            for a,b in arr:
                if grid1[a][b] == 0:
                    valid = False
                    break
            if valid:
                count += 1
        return count

