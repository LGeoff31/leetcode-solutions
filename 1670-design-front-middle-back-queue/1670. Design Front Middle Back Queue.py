class FrontMiddleBackQueue:
    """
    [2]
    """
    def __init__(self):
        self.queue1 = deque([])
        self.queue2 = deque([])
    
    def rebalance(self):
        # Invariant: queue1 should always be >= queue2 by at most 1
        if len(self.queue1) < len(self.queue2):
            self.queue1.append(self.queue2.popleft())
        elif len(self.queue1) - len(self.queue2) == 2:
            self.queue2.appendleft(self.queue1.pop())
        
    def pushFront(self, val: int) -> None:
        self.queue1.appendleft(val)
        self.rebalance()

    def pushMiddle(self, val: int) -> None:
        if len(self.queue1) > len(self.queue2):
            self.queue2.appendleft(self.queue1.pop())
        self.queue1.append(val)
        self.rebalance()

    def pushBack(self, val: int) -> None:
        self.queue2.append(val)
        self.rebalance()

    def popFront(self) -> int:
        if len(self.queue1) == 0:
            return -1

        val = self.queue1.popleft()
        self.rebalance()
        return val

    def popMiddle(self) -> int:
        if len(self.queue1) == 0:
            return -1
        
        val = self.queue1.pop()
        self.rebalance()
        return val
            

    def popBack(self) -> int:
        if len(self.queue1) == 0:
            return -1
        val = self.queue2.pop() if self.queue2 else self.queue1.pop()
        self.rebalance()
        return val


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()