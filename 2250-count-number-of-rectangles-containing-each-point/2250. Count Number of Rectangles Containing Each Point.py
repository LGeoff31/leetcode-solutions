class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        dic2 = defaultdict(list)
        rectangles.sort()
        for i in range(1, 101):
            for idx, (l, h) in enumerate(rectangles):
                if h >= i:
                    dic[i].append(idx) # Sorted
                    dic2[i].append(rectangles[idx][0])
        res = []

        for x,y in points:
            indicies = dic[y]
            widths = dic2[y]
            # for idx in indicies:
            #     widths.append(rectangles[idx][0])
            # print(indicies)
            res.append(len(indicies) -  bisect_left(widths, x))

        return res