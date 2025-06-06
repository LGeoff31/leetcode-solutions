from threading import Condition
class BoundedBlockingQueue(object):
    def __init__(self, capacity: int):
        self.queue = deque()
        self.condition = Condition()
        self.capacity = capacity
        
    def enqueue(self, element: int) -> None:
        self.condition.acquire()

        while self.size() == self.capacity:
            self.condition.wait()
        self.queue.append(element)
        self.condition.notify_all()
        self.condition.release()        

    def dequeue(self) -> int:
        self.condition.acquire()

        while self.size() == 0:
            self.condition.wait()
        
        output = self.queue.popleft()
        self.condition.notify_all()
        self.condition.release()
        return output
        

    def size(self) -> int:
        return len(self.queue)