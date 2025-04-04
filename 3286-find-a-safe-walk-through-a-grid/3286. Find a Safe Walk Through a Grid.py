class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        rows, cols = len(grid), len(grid[0])
        maxHeap = []
        heappush(maxHeap, (-1*(health - (grid[0][0] == 1)), 0, 0))
        visited = set()
        visited.add((0,0))
        # print(maxHeap)
        while maxHeap:
            h, r, c = heappop(maxHeap)
            h *= -1
            if r == rows-1 and c == cols-1 and h > 0: return True
            for new_r, new_c in [(r-1, c), (r+1, c), (r, c+1), (r,c-1)]:
                if 0<=new_r<rows and 0<=new_c<cols and (new_r, new_c) not in visited:
                    visited.add((new_r, new_c))
                    is_one = grid[new_r][new_c] == 1
                    heappush(maxHeap, (-(h-is_one), new_r, new_c))
            # print(maxHeap)
        return False
                 