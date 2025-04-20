class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        # Store the coordinates of all the ones
        # Use a nested loop to find all the pairs of ones
        # Assume that these two coordinates are diagonal, aka (c1 != c2, and r1 != r2)
        # You can easily tell what the other two missing coordinates
        # Do a lookup in hashmap for them
        # If exist add res
        # O(rc)
        # Claim: You'll never have more rectangles than cells on the board NVM
        
        rows, cols = len(grid), len(grid[0])
        dic = defaultdict(int)
        # Auto populate first one
        for c1 in range(cols):
            for c2 in range(c1 + 1, cols):
                if grid[0][c1] == grid[0][c2] == 1:
                    dic[(c1, c2)] += 1
        res = 0
        for r in range(1, rows):
            for c1 in range(cols):
                for c2 in range(c1 + 1, cols):
                    if grid[r][c1] == grid[r][c2] == 1:
                        res += dic[(c1, c2)]
                        dic[(c1, c2)] += 1
        return res