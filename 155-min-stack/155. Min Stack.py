class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val+1))
        self.stack.append((val, min(val, self.getMin())))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:   
        return self.stack[-1][0]     

    def getMin(self) -> int:
        return self.stack[-1][1]
        
"""
Node
value
pointer to prev & next
next smaller number

linkedlist is head -> tail in order of the simulated stack
min variable ; Node

[-2, -8, -3, 12, 17, 0, -100]


getMin -> -100
pop 
getMin -> -8
"""

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()