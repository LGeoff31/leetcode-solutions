class HitCounter:
    def __init__(self):
        self.queue = deque([])
        
    def flush(self, current_time):
        while self.queue and self.queue[0] <= current_time - 300:
            self.queue.popleft()

    def hit(self, timestamp: int) -> None:
        self.queue.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        self.flush(timestamp)
        return len(self.queue)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)