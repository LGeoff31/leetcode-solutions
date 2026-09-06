class Solution:
    def minCost(self, grid: list[list[int]], k: int) -> int:
        """
        want the mnimum, seems like dp. but we can also revist cells ?
        why would you ever want to revist a cell though, that makes no sense, unless negative values ? there all > 0
        
        2 7 3
        1 4 5

        4 1 9
        3 2 5
        4 8 6

        implement shortest path instead via dikstra
        """
        rows, cols = len(grid), len(grid[0])
        distance = {}
        state = (0, 0, -1, 0) # (r, c, last_dir, turns_used)
        minHeap = [(grid[0][0], 0, 0, -1, 0)]
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while minHeap:
            cost, r, c, last_dir, turned = heappop(minHeap)
            if cost > distance.get((r,c,last_dir,turned), 1e9):
                continue 

            if r == rows - 1 and c == cols - 1:
                return cost 

            for i, (dr, dc) in enumerate(directions):
                new_r, new_c = r + dr, c + dc
                if not (0 <= new_r < rows and 0 <= new_c < cols):
                    continue 

                new_turns = turned + (1 if last_dir != -1 and i != last_dir else 0)
                if new_turns > k:
                    continue 
                new_cost = cost + grid[new_r][new_c]

                if new_cost < distance.get((new_r, new_c, i, new_turns), 1e9):
                    distance[(new_r,new_c,i,new_turns)] = new_cost
                    heappush(minHeap, (new_cost, new_r, new_c, i, new_turns))
        return -1
        # def dfs(r,c, previous_direction, visited, directions_used):
        #     if directions_used > k:
        #         return 1e9
                
        #     if r == rows - 1 and c == cols - 1:
        #         return 0


        #     res = 1e9

        #     for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        #         new_r, new_c = r+dr, c+dc
        #         if not (0 <= new_r < rows and 0 <= new_c < cols) or (new_r,new_c) in visited:
        #             continue 
        #         val = grid[new_r][new_c]
        #         visited.add((new_r, new_c))
        #         if (dr, dc) != previous_direction and previous_direction != tuple():
        #             res = min(res, val + dfs(new_r, new_c, (dr, dc), visited, directions_used + 1))
        #         else:
        #             res = min(res, val + dfs(new_r, new_c, (dr, dc), visited, directions_used))
        #         visited.remove((new_r, new_c))
        #     return res    
        # res = grid[0][0] + dfs(0, 0, tuple(), set(), 0)
        # return res if res < 1e9 else -1
