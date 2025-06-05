class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_size = 0
        seen = set() #(i, j)

        def find_island_size(i: int, j: int) -> int:
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or (i, j) in seen or grid[i][j] == 0:
                return 0
            seen.add((i, j))
            size = 1
            size += find_island_size(i + 1, j)
            size += find_island_size(i - 1, j)
            size += find_island_size(i, j + 1)
            size += find_island_size(i, j - 1)
            return size
            
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) in seen:
                    continue
                if grid[i][j] == 1: 
                    size = find_island_size(i, j)
                    print("Size from "+ str(i) + " " + str(j) + " is: "+ str(size) )
                    if size > max_size:
                        max_size = size
                else:
                    seen.add((i, j))

        return max_size