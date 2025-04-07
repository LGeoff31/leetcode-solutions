class Router:

    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.seen = set()
        self.queue = deque([])
        self.dic = defaultdict(SortedList) # destination : SortedList([95, 100, 105])
        

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool: # O(1)
        if (source, destination, timestamp) in self.seen:
            return False
        if len(self.queue) == self.memoryLimit:
            a,b,c = self.queue.popleft()
            self.seen.remove((a,b,c))
            self.dic[b].remove(c)
            
        self.seen.add((source, destination, timestamp))
        self.queue.append((source, destination, timestamp))
        self.dic[destination].add(timestamp)

        return True

    def forwardPacket(self) -> List[int]: #O(1)
        if not self.queue: return []
        a,b,c = self.queue.popleft()
        self.seen.remove((a,b,c))
        self.dic[b].remove(c)
        return [a,b,c]
        

    def getCount(self, destination: int, startTime: int, endTime: int) -> int: #O(n) we need to implement BS
        count = 0
        sorted_arr = self.dic[destination]
        left_idx = bisect_left(sorted_arr, startTime)
        right_idx = bisect_right(sorted_arr, endTime)
        # print(sorted_arr)
        return right_idx - left_idx 
      
        


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)