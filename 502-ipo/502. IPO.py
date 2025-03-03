class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capitals: List[int]) -> int:
        lst = [(c, p) for c,p in zip(capitals, profits)]
        lst.sort()
        maxHeap = []
        i = 0
        # Initialize the minHeap with all the projects we can complete

        
        for _ in range(k):
            while i < len(capitals) and w >= lst[i][0]:
                heapq.heappush(maxHeap, (-lst[i][1], lst[i][0]))
                i += 1
                
            if not maxHeap:
                break
            p, c = heapq.heappop(maxHeap) #
            w -= p

        return w