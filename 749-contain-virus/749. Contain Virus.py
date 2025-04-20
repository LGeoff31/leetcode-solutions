class Solution:
    def containVirus(self, grid: List[List[int]]) -> int:
        # put in graph and know how much infected in each
        # use maxHeap determine where add walls
        # algorithm give # walls given a geometric virus orientation
        res = 0     
        rows, cols = len(grid), len(grid[0])
        def get_nei(r,c):
            for new_r, new_c in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if 0 <= new_r < rows and 0 <= new_c < cols:
                    yield (new_r, new_c)
        
        def dfs(r,c):
            if (r,c) not in seen:
                seen.add((r,c))
                regions[-1].add((r,c))
                for nei_r, nei_c in get_nei(r,c):
                    if grid[nei_r][nei_c] == 1:
                        dfs(nei_r, nei_c)
                    elif grid[nei_r][nei_c] == 0:
                        f[-1].add((nei_r, nei_c))
                        p[-1] += 1
        while True:
            # 1. Find all connected components
            seen = set()
            regions = []
            f = []
            p = []
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 1 and (r,c) not in seen:
                        regions.append(set())
                        f.append(set())
                        p.append(0)
                        dfs(r,c)
            if not regions:
                break
            
            # 2. Pick walls on the region with largest contamination
            idx = f.index(max(f, key = len))
            res += p[idx]
            # 3. Simulate all other walls getting expanded except one we encapulsated
            for i in range(len(regions)):
                if i == idx:
                    for r,c in regions[i]:
                        grid[r][c] = -1
                else:
                    for r, c in regions[i]:
                        for nei_r, nei_c in get_nei(r,c):
                            if grid[nei_r][nei_c] == 0:
                                grid[nei_r][nei_c] = 1

        return res