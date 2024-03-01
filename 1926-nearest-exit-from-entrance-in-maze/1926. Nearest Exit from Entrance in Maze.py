from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        queue = deque([entrance])
        rows, cols = len(maze), len(maze[0])
        visited = set()
        visited.add((entrance[0], entrance[1]))
        moves = 1
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                for d_r, d_c in [(1,0), (-1,0), (0,1), (0,-1)]:
                    new_r, new_c = r+d_r, c+d_c

                    if 0<=new_r<rows and 0<=new_c<cols and maze[new_r][new_c] == "." and (new_r,new_c) not in visited:
                        visited.add((new_r, new_c))
                        if new_r == 0 or new_c == 0 or new_r == rows - 1 or new_c == cols-1:
                            return moves
                        queue.append([new_r, new_c])
            moves += 1
        return -1
            



        