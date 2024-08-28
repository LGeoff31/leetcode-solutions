class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1: return -1
        rows, cols = len(grid), len(grid[0])
        direction = [[1,0], [0,1], [-1,0], [0,-1], [1,1], [-1,-1], [1,-1], [-1,1]]
        queue = deque([[0,0]])
        visited = set()
        count = 1
        while queue:
            for i in range(len(queue)):
                r1,c1 = queue.popleft()
                if r1==rows-1 and c1 == cols-1:
                    return count
                for r2, c2 in direction:
                    if 0<=r1+r2<rows and 0<=c1+c2<cols and grid[r1+r2][c1+c2] == 0 and (r1+r2, c1+c2) not in visited:
                        queue.append([r1+r2, c1+c2])
                        visited.add((r1+r2, c1+c2))
            count += 1
        return -1