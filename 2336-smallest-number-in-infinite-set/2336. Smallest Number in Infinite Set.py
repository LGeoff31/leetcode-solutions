class SmallestInfiniteSet:

    def __init__(self):
        self.arr = list(range(1,10000))

    def popSmallest(self) -> int:
        self.arr.sort()
        if self.arr:
            smallest = self.arr[0]
            self.arr = self.arr[1:]
            return smallest
        return 1


    def addBack(self, num: int) -> None:
        if num not in self.arr:
            self.arr.append(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)