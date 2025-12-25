class MinStack:
    def __init__(self):
        self.stack = []
        self.minValue = float('inf')

    def push(self, val: int) -> None:
        if val < self.minValue:
            self.stack.append((val, self.minValue))
            self.minValue = val
        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        a,b = self.stack.pop()
        if a == self.minValue:
            self.minValue = b

    def top(self) -> int:   
        return self.stack[-1][0]     

    def getMin(self) -> int:
        return self.minValue
        
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