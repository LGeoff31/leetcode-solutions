class MedianFinder:
    def __init__(self):
        self.minHeap = [] # Store later half of the array
        self.maxHeap = [] # Store start half of the array
    
    def addNum(self, num: int) -> None: # O(logn)
        # Want to ensure the two heaps are balanced or maxHeap has 1 more element
        heappush(self.maxHeap, -num)

        if self.minHeap and self.maxHeap and (-self.maxHeap[0] > self.minHeap[0]):
            val = -heappop(self.maxHeap)
            heappush(self.minHeap, val)
        
        if len(self.maxHeap) > len(self.minHeap) + 1:
            val = -heappop(self.maxHeap)
            heappush(self.minHeap, val)
        if len(self.minHeap) > len(self.maxHeap):
            val = heappop(self.minHeap)
            heappush(self.maxHeap, -val)
        
    def findMedian(self) -> float: # O(1)
        if (len(self.minHeap) + len(self.maxHeap)) % 2 == 1:
            return -self.maxHeap[0]
        return (-self.maxHeap[0] + self.minHeap[0]) / 2
       
       
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()