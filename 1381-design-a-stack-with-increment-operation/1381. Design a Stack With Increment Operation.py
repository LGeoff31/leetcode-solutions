class CustomStack:

    def __init__(self, maxSize: int):
        self.lst = []
        self.maxSize = maxSize
        

    def push(self, x: int) -> None:
        if len(self.lst) < self.maxSize:
            self.lst.append(x)    

    def pop(self) -> int:
        if self.lst:
            return self.lst.pop()
        return -1
       
        
    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.lst))):
            self.lst[i] += val
        
      