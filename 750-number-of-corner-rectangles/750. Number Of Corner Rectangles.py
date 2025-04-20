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
        
        rows = [[c for c, val in enumerate(row) if val]
                for row in grid]
        print(rows)
        N = sum(len(row) for row in grid)
        SQRTN = int(N**.5)
        print(N)
        ans = 0
        count = collections.Counter()
        for r, row in enumerate(rows):
            if len(row) >= SQRTN:
                target = set(row)
                for r2, row2 in enumerate(rows):
                    if r2 <= r and len(row2) >= SQRTN:
                        continue
                    found = sum(1 for c2 in row2 if c2 in target)
                    ans += found * (found - 1) / 2
            else:
                for pair in itertools.combinations(row, 2):
                    ans += count[pair]
                    count[pair] += 1

        return int(ans)