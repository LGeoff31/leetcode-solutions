class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        """
        the number of 2x2 matricies is (m-1) * (n-1), m>=2, n>=2
        """
        res = [0] * 5
        black_squares = set((r,c) for r, c in coordinates)
        seen = set()
        for r,c in black_squares:
            # TOP LEFT
            if r-1>=0 and c-1>=0 and (r-1,c-1) not in seen:
                cnt = ((r-1,c-1) in black_squares) + ((r-1,c) in black_squares) + ((r,c-1) in black_squares) + ((r,c) in black_squares)
                seen.add((r-1, c-1))
                res[cnt] += 1
            # TOP RIGHT
            if r-1>=0 and c < n-1 and (r-1,c) not in seen:
                cnt = ((r-1,c) in black_squares) + ((r,c) in black_squares) + ((r,c+1) in black_squares) + ((r-1,c+1) in black_squares)
                res[cnt] += 1
                seen.add((r-1, c))
            # TOP RIGHT
            if c-1>=0 and r < m-1 and (r,c-1) not in seen:
                cnt = ((r,c-1) in black_squares) + ((r,c) in black_squares) + ((r+1,c-1) in black_squares) + ((r+1,c) in black_squares)
                res[cnt] += 1
                seen.add((r, c-1))
            # TOP RIGHT
            if (r+1 < m) and (c+1 < n) and (r, c) not in seen:
                cnt = 1
                cnt += ((r+1, c) in black_squares) +  ((r+1, c+1) in black_squares) +  ((r, c+1) in black_squares)  
                res[cnt] += 1
                seen.add((r,c))

        res[0] = (m-1) * (n-1) - sum(res)

        return res
