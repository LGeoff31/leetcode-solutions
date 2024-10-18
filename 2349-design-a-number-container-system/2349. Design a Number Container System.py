from sortedcontainers import SortedList
class NumberContainers:

    def __init__(self):
        self.dic = defaultdict(SortedList)
        self.dic2 = {}
        

    def change(self, index: int, number: int) -> None:
        if index in self.dic2:
            self.dic[self.dic2[index]].remove(index)
        self.dic[number].add(index)
        self.dic2[index] = number
        

    def find(self, number: int) -> int:
        if number not in self.dic or not self.dic[number]:
            return -1
        return self.dic[number][0]


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)