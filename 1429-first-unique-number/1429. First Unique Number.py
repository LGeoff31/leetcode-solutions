from collections import deque

class FirstUnique:

    def __init__(self, nums: List[int]):
        self._queue = deque(nums)
        self._is_unique = {}
        for num in nums:
            # Notice that we're calling the "add" method of FirstUnique; not of the queue. 
            self.add(num)
        
    def showFirstUnique(self) -> int:
        # We need to start by "cleaning" the queue of any non-uniques at the start.
        # Note that we know that if a value is in the queue, then it is also in
        # is_unique, as the implementation of add() guarantees this.
        while self._queue and not self._is_unique[self._queue[0]]:
            self._queue.popleft()
        # Check if there is still a value left in the queue. There might be no uniques.
        if self._queue:
            return self._queue[0] # We don't want to actually *remove* the value.
        return -1
        
    def add(self, value: int) -> None:
        # Case 1: We need to add the number to the queue and mark it as unique. 
        if value not in self._is_unique:
            self._is_unique[value] = True
            self._queue.append(value)
        # Case 2 and 3: We need to mark the number as no longer unique.
        else:
            self._is_unique[value] = False