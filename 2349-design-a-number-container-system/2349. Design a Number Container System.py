class NumberContainers:
    def __init__(self):
        self.dic = defaultdict(SortedList)
        self.index_to_number = {}

    def change(self, index: int, number: int) -> None:
        if index in self.index_to_number:
            num = self.index_to_number[index]
            self.dic[num].remove(index)
        self.index_to_number[index] = number
        self.dic[number].add(index)

    def find(self, number: int) -> int:
        lst = self.dic[number]
        if not lst: return -1
        return lst[0]
     