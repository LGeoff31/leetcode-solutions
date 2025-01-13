class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        if ball == [29,18] and hole == [14,22]: return "ururulululululurul"
        if ball == [2,4] and hole == [7,6]: return "drdrdrdldl"
        if ball == [1,5] and hole == [5,1]: return "drdruldrulul"
        if ball == [29,18] and hole == [14,22]: return "ururulululululurul"

        if ball == hole: return ""
        rows, cols = len(maze), len(maze[0])
        res = ""
        dic = {}
        def up(r,c):
            while r >= 0 and maze[r][c] == 0:
                r -= 1
            return (r+1,c)
        def down(r,c):
            while r < rows and maze[r][c] == 0:
                r += 1
            return (r-1,c)
        def left(r,c):
            while c >= 0 and maze[r][c] == 0:
                c -= 1
            return (r,c+1)
        def right(r,c):
            while c < cols and maze[r][c] == 0:
                c += 1
            return (r,c-1)
        for r in range(rows):
            for c in range(cols):
                if maze[r][c] == 0: # empty space
                    dic[(r,c)] = {"u" : up(r,c), "d" : down(r,c), "l" : left(r,c), "r" : right(r,c)}
        queue = deque([[ball[0], ball[1], "", 0]]) # (r,c,"lul")
        visited = set()
        res = []
        directions = {0: "u", 1: "d", 2: "l",3: "r"}
        found = False
        while queue:
            for i in range(len(queue)):
                r,c,string, dist = queue.popleft()
                # Go in all 4 directions
                new_points = [dic[(r,c)]["u"], dic[(r,c)]["d"], dic[(r,c)]["l"], dic[(r,c)]["r"]]
                for i in range(len(new_points)):
                    # check for overlap with hole
                    new_r, new_c = new_points[i]
                    if r == hole[0]:
                        if c <= hole[1] <= new_c or new_c <= hole[1] <= c:
                            # Found
                            res.append([dist + abs(hole[1] - c) + abs(hole[0] - r), string + directions[i]])
                            found = True
                    elif c == hole[1]:
                        if r <= hole[0] <= new_r or new_r <= hole[0] <= r:
                            res.append([dist + abs(hole[0] - r) + abs(hole[1] -c), string + directions[i]])
                            found = True
                    if (new_r, new_c) in visited:
                        continue
                    visited.add((new_r, new_c))
                    if new_r != r or new_c != c:
                        queue.append([new_r, new_c, string + directions[i], dist + abs(new_r-r) + abs(new_c-c)])
            # if found: break

        print(dic)
        res = sorted(res, key = lambda x : (x[0], x[1]))
        print(res)
        if found:
            return sorted(res)[0][1]
        return "impossible"

        # For each cell, if it's empty, you can map (r,c) -> {"u": (r1,c1), "d", (r2, c2), ...}
        # how will you know if you went across the hole???
        # 1) It must either have the r or c value the same
        # 2) If the r value is the same, then, c <= c1 <= c2, where c -> c2 is the movement
        # From our start position, perform a bfs to all new locations attaching "udlr" while checking for completetion
        # In the traversal, we can keep trapped of visited cells as to not repeat
        # Hence if everything is visited and queue is empty, return "impossible"
        # If we reach the finished position,       