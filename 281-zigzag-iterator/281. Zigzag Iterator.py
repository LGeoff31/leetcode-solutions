class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.i, self.j = 0, 0
        self.look_v1 = True
        self.v1 = v1
        self.v2 = v2

    def next(self) -> int:
        val = -1
        print('called')
        if self.look_v1:
            if self.i < len(self.v1):
                val = self.v1[self.i]
                self.i += 1
            else:
                val = self.v2[self.j]
                self.j += 1
        else:
            if self.j < len(self.v2):
                val = self.v2[self.j]
                self.j += 1
            else:
                val = self.v1[self.i]
                self.i += 1
                    
        self.look_v1 = not self.look_v1
        return val

    def hasNext(self) -> bool:
        return self.i < len(self.v1) or self.j < len(self.v2)

        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())