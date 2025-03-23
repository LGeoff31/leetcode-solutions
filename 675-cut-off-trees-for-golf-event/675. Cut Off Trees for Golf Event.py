class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        if forest[0][0] == 0: return -1
        rows, cols = len(forest), len(forest[0])
        minHeap = []
        for r in range(rows):
            for c in range(cols):
                if forest[r][c] > 1:
                    heappush(minHeap, (forest[r][c], r, c))
        def numberSteps(r,c,nxt_r,nxt_c):
            visited = set()
            visited.add((r,c))
            queue = deque([(r,c,0)])
            while queue:
                r,c,steps = queue.popleft()
                if r == nxt_r and c == nxt_c:
                    forest[r][c] = 1
                    return steps
                
                for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    new_r, new_c = r+dr, c+dc
                    if 0<=new_r<rows and 0<=new_c<cols and forest[new_r][new_c] != 0 and (new_r, new_c) not in visited:
                        visited.add((new_r, new_c))
                        queue.append((new_r, new_c, steps + 1))
                # print(queue)
            return -1
        r,c = 0, 0
        res = 0
        while minHeap:
            _,nxt_r,nxt_c = heappop(minHeap)
            nxtSteps = numberSteps(r,c,nxt_r,nxt_c) 
            # print(nxtSteps, r,c,nxt_r,nxt_c)
            if nxtSteps == -1:
                return -1
            res += nxtSteps
            r,c = nxt_r,nxt_c
        return res
            