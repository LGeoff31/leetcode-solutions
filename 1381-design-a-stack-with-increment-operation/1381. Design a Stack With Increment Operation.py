class CustomStack:
    def __init__(self, maxSize: int):
        self.lst = []
        self.maxSize = maxSize
        self.inc = []
        

    def push(self, x: int) -> None:
        if len(self.lst) < self.maxSize:
            self.lst.append(x)    
            self.inc.append(0)

    def pop(self) -> int:
        if not self.lst: return -1
        if len(self.inc) > 1:
            self.inc[-2] += self.inc[-1]
        return self.lst.pop() + self.inc.pop()
       
    def increment(self, k: int, val: int) -> None:
        if self.inc: self.inc[min(k-1, len(self.lst) - 1)] += val
        
      