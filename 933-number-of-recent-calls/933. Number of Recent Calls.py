from collections import deque
class RecentCounter:

    def __init__(self):
        self.requests = deque([])
        self.counter = 0

        

    def ping(self, t: int) -> int:
        self.counter += 1
        self.requests.append(t) #[1,100, 3001, 3002]

        while self.requests[0] < t-3000: #2, 3002
            self.counter -= 1
            self.requests.popleft()
        return self.counter

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)