class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        queue = deque([[0,0]])
        rows, cols = len(grid), len(grid[0])


        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        dictionary = {(0, 0) : health - grid[0][0]}

        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if (nr, nc) not in dictionary:
                            dictionary[(nr, nc)] = dictionary[(r,c)] + (-1 if grid[nr][nc] == 1 else 0)
                            queue.append([nr, nc])
                        elif (nr, nc) in dictionary and dictionary[(r,c)] + (-1 if grid[nr][nc] == 1 else 0) > dictionary[(nr,nc)]:
                            dictionary[(nr, nc)] = dictionary[(r,c)] + (-1 if grid[nr][nc] == 1 else 0)
                            queue.append([nr, nc])

        print(dictionary)
        if (rows-1, cols-1) in dictionary and dictionary[(rows-1, cols-1)] > 0:
            return True
        return False