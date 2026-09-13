class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        img1_ones = set()
        img2_ones = set()
        n = len(img1)

        for r in range(n):
            for c in range(n):
                if img1[r][c] == 1:
                    img1_ones.add((r,c))
                if img2[r][c] == 1:
                    img2_ones.add((r,c))

        res = 0
        cache = set()
        for r1, c1 in img1_ones:
            for r2, c2 in img2_ones:
                dr = r2 - r1
                dc = c2 - c1
                if (dr, dc) in cache:
                    continue
                cache.add((dr, dc))

                cnt = 0
                for r2, c2 in img2_ones:
                    cnt += (r2-dr, c2-dc) in img1_ones
                res = max(res, cnt)
        return res
                        

