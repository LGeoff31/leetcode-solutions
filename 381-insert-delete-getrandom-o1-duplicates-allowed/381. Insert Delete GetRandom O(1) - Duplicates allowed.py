class RandomizedCollection:
    def __init__(self):
        self.dic = defaultdict(SortedList)
        self.lst = []

    def insert(self, val: int) -> bool:
        not_present = not(self.dic[val])
        self.lst.append(val)
        self.dic[val].add(len(self.lst) - 1)
        return not_present

    def remove(self, val: int) -> bool:
        if not self.dic[val]:
            return False 
        idx = self.dic[val][-1]
        last_val = self.lst[-1]
        self.lst[idx], self.lst[-1] = self.lst[-1], self.lst[idx]
        if idx != len(self.lst) - 1:
            self.dic[last_val].pop()
            self.dic[last_val].add(idx)

        self.lst.pop()
        self.dic[val].pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.lst)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

"""
[2, 2, 2, 1]

{1: [0], 2: [2,3,0]}
"""