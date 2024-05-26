class MyCalendar:
    def __init__(self):
        self.lst = []
        
    def book(self, start: int, end: int) -> bool:
        for s,e in self.lst:
            if s >= end or start >= e:
                continue
            else:
                return False
        self.lst.append([start, end])
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)