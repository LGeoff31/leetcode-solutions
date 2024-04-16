from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        self.lst = SortedList()
        

    def addNum(self, num: int) -> None:
        self.lst.add(num)
        

    def findMedian(self) -> float:
        idx = len(self.lst) // 2
        if len(self.lst)%2==0:
            return (self.lst[idx-1] + self.lst[idx])/2
        return self.lst[idx]

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()