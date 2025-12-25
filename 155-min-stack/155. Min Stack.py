class Node:
    def __init__(self, value, prev, minElem):
        self.prev = prev
        self.val = (value, minElem)

class MinStack:
    def __init__(self):
        self.tail = None

    def push(self, val: int) -> None:
        if self.tail is None:
            self.tail = Node(val, None, val)
        else:
            newNode = Node(val, self.tail, min(val, self.getMin()))
            newNode.prev = self.tail
            self.tail = newNode

    def pop(self) -> None:
        self.tail = self.tail.prev

    def top(self) -> int:   
        return self.tail.val[0]    

    def getMin(self) -> int:
        if self.tail:
            return self.tail.val[1]
        return None
        
"""
0, 1, -2, -1
Node
value
pointer to prev & next
next smaller number

linkedlist is head -> tail in order of the simulated stack
min variable ; Node

[-2, -8, -3, 12, 17, 0, -100]
[-2, -8, -8, -8, -8, -8, -100]


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