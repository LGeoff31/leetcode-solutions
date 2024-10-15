class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # Shortest path finding algorithm from island 1 to island 2
        # For each of island 1, bfs into a new cell
        # If new cell is island 1, continue
        # If new cell is empty, add 1 to steps
        # If new cell is island 2, return amount of steps

        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        # Step 1: Find island 1
        island_1 = set()

        def bfs(r,c):
            queue = deque([[r,c]])
            island_1.add((r,c))
            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    new_r, new_c = row + dr, col + dc
                    # Ensure they are within the boundary and a 1 and not already added
                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1 and (new_r, new_c) not in island_1:
                        island_1.add((new_r, new_c))
                        queue.append([new_r, new_c])
                
        found = False
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    bfs(r,c) # This should populate island_1
                    found = True
                    break
            if found: break

        # Step 2: For each node in island 1, bfs to find the minimum number of cells to get to island 2
        island_1_coordiantes = list(island_1)
        res = 1e9

        def bfs_island_2(r,c):
            steps = 0
            visited = set()
            visited.add((r,c))
            queue = deque([[r,c]])
            while queue:
                for i in range(len(queue)):
                    row, col = queue.popleft()
                    for dr, dc in directions:
                        new_r, new_c = row+dr, col+dc
                        if 0 <= new_r < rows and 0 <= new_c < cols and (new_r, new_c) not in visited and (new_r, new_c) not in island_1:
                            visited.add((new_r, new_c))
                            if grid[new_r][new_c] == 1:
                                print('reached', new_r, new_c, r,c )
                                return steps
                            queue.append([new_r, new_c])
                if (r,c) == (0,0):
                    print(queue)
                steps += 1

            return 1e9 # Has not been found
        print(island_1_coordiantes)
        for r,c in island_1_coordiantes:
            print(r,c, bfs_island_2(r,c))
            res = min(res, bfs_island_2(r,c))

        return res