class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        # 0 2 3 1
        # 3 1 2 3
        # 3 4 1 2
        if not(grid[0][1] == 1 or grid[1][0] == 1 or grid[0][1] == 0 or grid[1][0] == 0): return -1

        minHeap = [(0, 0, 0)]
        visited = {}
        adj = defaultdict(list)

        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                # Add up
                if c-1 >= 0:
                    adj[(r,c)].append([r, c-1])
                # Add right
                if r+1 < rows:
                    adj[(r,c)].append([r+1, c])
                # Add down
                if c+1 < cols:
                    adj[(r,c)].append([r, c+1])
                # Add up
                if r-1 >= 0:
                    adj[(r,c)].append([r-1, c])

        while minHeap:
            currTime, r1, c1 = heappop(minHeap)
            # if (r1, c1) in visited:
            #     continue 
            # print(w1, r1, c1, visited, currTime)
            visited[(r1, c1)] = currTime
            # print(adj[(r1, c1)])
            for r2, c2 in adj[(r1, c1)]:
                # print(r2, c2)
                if (r2, c2) not in visited:
                    if  currTime+1 >= grid[r2][c2]:
                        # print(r2, c2)
                        heappush(minHeap, (currTime+1, r2, c2))
                        visited[(r2, c2)] = currTime+1
                    else:
                        # Must occilate to make up diff
                        diff = grid[r2][c2] - currTime 
                        if diff % 2 == 1:
                            heappush(minHeap, (grid[r2][c2], r2, c2))
                            visited[(r2, c2)] = grid[r2][c2]
                        else:
                            heappush(minHeap, (grid[r2][c2] + 1, r2, c2))
                            visited[(r2, c2)] = grid[r2][c2] + 1
            # print(visited)
        # print(visited)
        return visited[(rows-1, cols-1)]
        # return 0