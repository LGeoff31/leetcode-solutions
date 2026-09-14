class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # Basically, find overlap with X, find overlap with Y, there should be both to return True
        x_overlap = (rec1[0] <= rec2[0] < rec1[2]) or (rec2[0] <= rec1[0] < rec2[2])
        y_overlap = (rec1[1] <= rec2[1] < rec1[3]) or (rec2[1] <= rec1[1] < rec2[3])
        return x_overlap and y_overlap