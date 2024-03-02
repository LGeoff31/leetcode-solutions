from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #have minute counter
        #put all adjacent 4 cells in all inital rootten ttomates to be rotten
        #check make sure theres no 1's aka non rottens otherwise contiue
        #simply return minute counter
        visited = set()
        minutes = 0
        queue = deque([])
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append([r,c]) 
                    visited.add((r,c))
        oneCounts = 0
        for a in grid:
            if 1 in a:
                oneCounts += 1
        if oneCounts == 0:
            return 0
        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()
                if row-1 >= 0:
                    if (row-1, col) not in visited:
                        if grid[row-1][col] == 1:
                            grid[row-1][col] = 2
                            queue.append([row-1, col])
                            visited.add((row-1, col))
                if row+1 < len(grid):
                    if (row+1, col) not in visited:
                        if grid[row+1][col] == 1:
                            grid[row+1][col] = 2
                            queue.append([row+1, col])
                            visited.add((row+1, col))
                if col-1 >= 0:
                    if (row, col-1) not in visited:
                        if grid[row][col-1] == 1:
                            grid[row][col-1] = 2
                            queue.append([row, col-1])
                            visited.add((row,col-1))
                if col+1 < len(grid[0]):
                    if (row, col+1,) not in visited:
                        if grid[row][col+1] == 1:
                            grid[row][col+1] = 2
                            queue.append([row, col+1])
                            visited.add((row,col+1))
            minutes += 1
            oneCounts = 0
            for a in grid:
                if 1 in a:
                    oneCounts += 1
                    break
            if oneCounts == 0:
                return minutes
            print(queue)

        return -1