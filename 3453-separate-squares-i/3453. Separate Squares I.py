class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        min_y = min(b for _,b,_ in squares)
        max_y = max((b+c) for _,b,c in squares)
        total_area = sum(c**2 for _,_,c in squares)
        print(total_area, min_y, max_y)
        def areaAbove(mid_y):
            res = 0
            for x,y,length in squares:
                if y >= mid_y:
                    res += length ** 2
                elif y <= mid_y <= y+length:
                    res += (y+length - mid_y) * length

            return res
        res = 1e9
        while min_y <= max_y:
            mid_y = (min_y + max_y) / 2
            print(mid_y, areaAbove(mid_y))
            if areaAbove(mid_y) <= total_area / 2:
                max_y = mid_y - 1e-5
            else:
                min_y = mid_y + 1e-5

            # if abs(total_area / 2 - areaAbove(mid_y)) < 0.2:
            #     res = min(res, mid_y)
        
        return max_y
        
