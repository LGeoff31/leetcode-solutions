class MyQueue:
    def __init__(self):
        self.forward = []

    def push(self, x: int) -> None:
        self.forward.append(x)
        

    def pop(self) -> int:
        a = self.forward[0]
        self.forward = self.forward[1:]
        return a

    def peek(self) -> int:
        return self.forward[0]
        

    def empty(self) -> bool:
        return len(self.forward) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()