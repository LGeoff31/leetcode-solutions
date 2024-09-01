class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        # Expand the square using binary search??
        l, r = 0, 10 ** 9
        res = 0
        while l <= r:
            mid = l + (r-l) // 2
            # Check if a square with side length mid is valid
            a = set()
            valid = True
            for i, (x,y) in enumerate(points):
                if max(abs(x),abs(y)) <= mid:
                    if s[i] in a:
                        valid = False
                        break
                    else:
                        a.add(s[i])

            print('trying', mid, valid, a)
            if valid:
                res = max(res, len(a))
                l = mid + 1
            else:
                r = mid - 1
        return res