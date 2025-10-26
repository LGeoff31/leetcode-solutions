class MyCircularQueue:
    def __init__(self, k: int):
        self.k = k
        self.array = [-1] * k
        self.head = 0
        self.tail = 0
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.head != self.tail or self.count == 0:
            self.array[self.head] = value
            self.head = (self.head + 1) % self.k
            self.count += 1
            return True
        return False

    def deQueue(self) -> bool:
        if self.tail != self.head or self.count == self.k:
            self.array[self.tail] = -1
            self.tail = (self.tail + 1) % self.k
            self.count -= 1
            return True
        return False

    def Front(self) -> int:
        return self.array[self.tail%self.k]

    def Rear(self) -> int:
        return self.array[(self.head-1)%self.k]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool: 
        return self.count == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()