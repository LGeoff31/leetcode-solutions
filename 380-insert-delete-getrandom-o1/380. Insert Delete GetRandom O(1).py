class RandomizedSet:
    def __init__(self):
        self.dic = {} # Num : idx
        self.arr = []
        

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False 
        self.arr.append(val)
        self.dic[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        print()
        # print(self.arr, self.dic)
        if val not in self.dic:
            return False
        idx = self.dic[val]
        self.arr[idx], self.arr[-1] = self.arr[-1], self.arr[idx]
        self.arr.pop()
        if idx < len(self.arr):
            self.dic[self.arr[idx]] = idx

        del self.dic[val]
        return True

    def getRandom(self) -> int:
        # print(self.arr)
        return self.arr[randint(0, len(self.arr) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()