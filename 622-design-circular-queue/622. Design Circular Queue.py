class MyCircularQueue:
    """
    [None, None, None]
   t h 
    """
    def __init__(self, k: int):
        self.k = k
        self.size = 0
        self.tail = 0
        self.head = 0
        self.circular_buffer = [0] * k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False 
        self.circular_buffer[self.head] = value
        self.head = (self.head + 1) % self.k
        self.size += 1
        return True 

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False 
        self.circular_buffer[self.tail] = None
        self.tail = (self.tail + 1) % self.k
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.circular_buffer[self.tail]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.circular_buffer[self.head - 1]
        
    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()