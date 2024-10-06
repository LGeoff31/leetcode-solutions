class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def intersect(x1,y1,r1,x2,y2,r2):
            radius_distance = r1 + r2
            x_dist = abs(x2-x1)
            y_dist = abs(y2-y1)
            total_dist = math.sqrt(x_dist**2 + y_dist**2)
            return total_dist <= r1
        
        def find_nei(idx):
            x,y,r = bombs[idx]
            lst = []
            for i in range(len(bombs)):
                if i == idx:
                    continue
                if intersect(x,y,r, bombs[i][0], bombs[i][1], bombs[i][2]):
                    lst.append(i)
            return lst
        
        def dfs(i):
            stack = [i]
            visited = set([i])
            while stack:
                node = stack.pop()
                for nei in find_nei(node):
                    if nei not in visited:
                        visited.add(nei)
                        stack.append(nei)
            print(visited)
            return len(visited)
        
        res = 0
        for i in range(len(bombs)):
            res = max(res, dfs(i))
        return res

