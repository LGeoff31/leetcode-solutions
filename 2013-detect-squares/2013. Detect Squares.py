class DetectSquares:
    def __init__(self):
        self.points_count = defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        self.points_count[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        count = 0

        # Check for possible points to form a square
        for (x2, y2), freq in self.points_count.items():
            # Must be on the same vertical or horizontal axis (excluding the point itself)
            if abs(x1 - x2) != abs(y1 - y2) or x1 == x2 or y1 == y2:
                continue

            # Check if the other two points needed for the square exist
            if (x1, y2) in self.points_count and (x2, y1) in self.points_count:
                count += freq * self.points_count[(x1, y2)] * self.points_count[(x2, y1)]

        return count
            
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)