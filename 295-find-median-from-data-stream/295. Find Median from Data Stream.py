class MedianFinder:
    def __init__(self):
        # All elements in maxHeap <= all elements in minHeap
        # abs(len(minHeap) - len(maxHeap)) <= 1
        self.minHeap = []
        self.maxHeap = []
    
    def addNum(self, num: int) -> None: 
        # Base case
        if not self.maxHeap:
            heappush(self.maxHeap, -num)
            return

        if len(self.maxHeap) > len(self.minHeap): # Greater by 1
            heappush(self.minHeap, num)
            if -self.maxHeap[0] > self.minHeap[0]:
                temp1 = heappop(self.minHeap)
                temp2 = -heappop(self.maxHeap)
                heappush(self.maxHeap, -temp1)
                heappush(self.minHeap, temp2)
        elif len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap, -num)
            if -self.maxHeap[0] > self.minHeap[0]:
                temp1 = heappop(self.minHeap)
                temp2 = -heappop(self.maxHeap)
                heappush(self.maxHeap, -temp1)
                heappush(self.minHeap, temp2)
        else:
            if num <= self.minHeap[0]:
                heappush(self.maxHeap, -num)
            else:
                heappush(self.minHeap, num)

    def findMedian(self) -> float:
        if (len(self.minHeap) + len(self.maxHeap)) % 2 == 1:
            return self.minHeap[0] if len(self.minHeap) > len(self.maxHeap) else -self.maxHeap[0]
        return (-self.maxHeap[0] + self.minHeap[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()