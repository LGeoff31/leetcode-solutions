class MedianFinder:
    """
    Two heaps h1 and h2. Hold invariant that there abs(len(h1) - len(h2)) <= 1
    h1 will be a minHeap storing the larger portion numbers so far.
    h2 will be a maxHeap storing the smaller portion numbers so far.

    {1,4,6,8,5}

    h1 = {6, 8}
    h2 = {1, 4}

    """
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if not self.minHeap or not self.maxHeap:
            if self.minHeap: 
                if self.minHeap[0] < num:
                    n = heappop(self.minHeap)
                    heappush_max(self.maxHeap, n)
                    heappush(self.minHeap, num)
                else:
                    heappush_max(self.maxHeap, num)

            if self.maxHeap:
                if self.maxHeap[0] > num:
                    n = heappop_max(self.maxHeap)
                    heappush(self.minHeap, n)
                    heappush_max(self.maxHeap, num)
                else:
                    heappush(self.minHeap, num)
            
            if not self.minHeap and not self.maxHeap:
                heappush_max(self.maxHeap, num)
            return 
        
        larger_element = self.minHeap[0]
        smaller_element = self.maxHeap[0]
        if len(self.minHeap) == len(self.maxHeap):
            if num > larger_element:
                heappush(self.minHeap, num)
            else:
                heappush_max(self.maxHeap, num)
        elif len(self.minHeap) > len(self.maxHeap):
            if num > larger_element:
                n = heappop(self.minHeap)
                heappush_max(self.maxHeap, n)
                heappush(self.minHeap, num)
            else:
                heappush_max(self.maxHeap, num)
        else:
            if num < smaller_element:
                n = heappop_max(self.maxHeap)
                heappush(self.minHeap, n)
                heappush_max(self.maxHeap, num)
            else:
                heappush(self.minHeap, num)




    def findMedian(self) -> float:
        if not self.minHeap and not self.maxHeap: return 0
        if self.minHeap and not self.maxHeap: return self.minHeap[0]
        if not self.minHeap and self.maxHeap: return self.maxHeap[0]
        if (len(self.minHeap) + len(self.maxHeap)) % 2 == 1:
            return self.minHeap[0] if len(self.minHeap) > len(self.maxHeap) else self.maxHeap[0]
        return (self.minHeap[0] + self.maxHeap[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()