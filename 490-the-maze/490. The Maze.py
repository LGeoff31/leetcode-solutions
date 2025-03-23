class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # Run a BFS in all 4 directions to see new positions 
        # If new position is goal, return True
        # If you get to already seen position, have visited set 
        queue = deque([start])
        visited = set()
        # visited.add((start[0], start[1]))
        rows, cols = len(maze), len(maze[0])

        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                if (r,c) in visited: continue
                visited.add((r,c))
                if [r,c] == destination:
                    return True
                # Find neighbors

                # Going left
                new_r, new_c = r, c
                while new_c >= 0 and maze[new_r][new_c] != 1: new_c -= 1
                new_c += 1
                if (new_r, new_c) not in visited:
                    queue.append((new_r, new_c))
                
                # Going right
                new_r, new_c = r, c
                while new_c < cols and maze[new_r][new_c] != 1: new_c += 1
                new_c -= 1
                if (new_r, new_c) not in visited:
                    queue.append((new_r, new_c))
                
                # Going up
                new_r, new_c = r, c
                while new_r >= 0 and maze[new_r][new_c] != 1: new_r -= 1
                new_r += 1
                if (new_r, new_c) not in visited:
                    queue.append((new_r, new_c))
                
                # Going down
                new_r, new_c = r, c
                while new_r < rows and maze[new_r][new_c] != 1: new_r += 1
                new_r -= 1
                if (new_r, new_c) not in visited:
                    queue.append((new_r, new_c))
                print(queue)

        return False
        