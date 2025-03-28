class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        # O(Q * M * N)
        res = [0] * len(queries)
        queries = sorted([(queries[i], i) for i in range(len(queries))])
        rows, cols = len(grid), len(grid[0])
        minHeap = [(grid[0][0], 0, 0)]
        count = 0
        visited = set()
        visited.add((0,0))
        print(queries)
        for q, idx in queries:
            while minHeap and minHeap[0][0] < q:
                val, r, c = heappop(minHeap)
                count += 1
                for new_r, new_c in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if 0 <= new_r < rows and 0 <= new_c < cols and (new_r, new_c) not in visited:
                        visited.add((new_r, new_c))
                        heappush(minHeap, (grid[new_r][new_c], new_r, new_c))
            res[idx] = count
            print('count', count)
            
        return res