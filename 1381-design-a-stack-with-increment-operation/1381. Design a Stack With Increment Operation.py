class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.lst = []
        

    def push(self, x: int) -> None:
        if len(self.lst) < self.maxSize:
            self.lst.append(x)
        

    def pop(self) -> int:
        if self.lst:
            return self.lst.pop()
        return -1
        
    def increment(self, k: int, val: int) -> None:
        if len(self.lst) < k:
            for i in range(len(self.lst)):
                self.lst[i] += val
        else:
            for i in range(k):
                self.lst[i] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)