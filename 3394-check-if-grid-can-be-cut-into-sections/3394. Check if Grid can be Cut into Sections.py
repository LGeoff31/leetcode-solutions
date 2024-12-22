class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        # Try to make 2 horizontal cuts
        vertically_sorted_rectangles = sorted(rectangles, key=lambda x: x[1])
        horizontal_cuts = 0
        def overlap(rectangle1, rectangle2):
            return rectangle1[3] > rectangle2[1]
        i = 0
        farthest_y = vertically_sorted_rectangles[0][3]
        while i < len(vertically_sorted_rectangles):
            while (i+1) < len(vertically_sorted_rectangles) and (overlap(vertically_sorted_rectangles[i], vertically_sorted_rectangles[i+1]) or vertically_sorted_rectangles[i+1][1] < farthest_y):
                farthest_y = max(farthest_y, vertically_sorted_rectangles[i][3])
                i += 1
            i += 1
            if i >= len(vertically_sorted_rectangles): break
            farthest_y = max(farthest_y, vertically_sorted_rectangles[i][3])
            horizontal_cuts += 1

        # Try to make 2 vertical cuts
        horizontally_sorted_rectangles = sorted(rectangles, key=lambda x: x[0])
        print(horizontally_sorted_rectangles)
        vertical_cuts = 0
        def overlap(rectangle1, rectangle2):
            return rectangle1[2] > rectangle2[0]
        i = 0
        farthest_x = horizontally_sorted_rectangles[0][2]
        while i < len(horizontally_sorted_rectangles):
            # Keep track of the farthest most x value so far
            while (i+1) < len(horizontally_sorted_rectangles) and (overlap(horizontally_sorted_rectangles[i], horizontally_sorted_rectangles[i+1]) or horizontally_sorted_rectangles[i+1][0] < farthest_x):  
                farthest_x = max(farthest_x, horizontally_sorted_rectangles[i][2])
                i += 1
            i += 1
            if i >= len(horizontally_sorted_rectangles): break
            farthest_x = max(farthest_x, horizontally_sorted_rectangles[i][2])
            vertical_cuts += 1
        # print(horizontal_cuts, vertical_cuts)
        return horizontal_cuts >= 2 or vertical_cuts >= 2