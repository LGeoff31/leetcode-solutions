class UnionFind:
    def __init__(self):
        self.parent = {}
        self.size = {}
        self.number_islands = 0

    def find(self, x):
        self.parent.setdefault(x, x)
        self.size.setdefault(x, 1)

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        if x == y:
            self.number_islands += 1
        parent_x = self.find(x)
        parent_y = self.find(y)
        if parent_x != parent_y:
            self.number_islands -= 1
            if self.size[parent_x] < self.size[parent_y]:
                parent_x, parent_y = parent_y, parent_x
            self.size[parent_x] += self.size[parent_y]
            self.parent[parent_y] = parent_x
        
    def size(self, x):
        return self.size[x]

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        a = set()
        # new_positions = []
        cache = {}
        # for r,c in positions:
        #     if (r,c) not in a:
        #         a.add((r,c))
        #         new_positions.append((r,c))
        # positions = new_positions
        union_find = UnionFind()
        res = []
        grid = [[0] * n for _ in range(m)]
        for r, c in positions:
            if (r,c) in cache:
                res.append(res[-1])
                continue
            grid[r][c] = 1
            union_find.union((r,c), (r,c))
            for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                new_r = r + dr
                new_c = c + dc
                if 0 <= new_r < m and 0 <= new_c < n and grid[new_r][new_c] == 1:
                    union_find.union((r,c), (new_r, new_c))
            cache[(r,c)] = union_find.number_islands
            res.append(union_find.number_islands)

        return res
