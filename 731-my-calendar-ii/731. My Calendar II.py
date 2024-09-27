class MyCalendarTwo:
    def __init__(self):
        self.overlapping = []
        self.nonoverlapping = []
        

    def book(self, start: int, end: int) -> bool:
        for s, e in self.overlapping:
            if not(start >= e or s >= end): # Triple Overlap
                return False
        for s, e in self.nonoverlapping:
            # Find if there's an intersection
            if not(start >= e or s >= end):
                self.overlapping.append((max(start, s), min(end, e)))
        self.nonoverlapping.append((start, end))
        return True

        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)