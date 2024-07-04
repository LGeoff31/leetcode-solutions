class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        res = 0
        minHeap = []
        events.sort()
        today = 0
        i = 0
        n = len(events)

        while minHeap or i < n:
            if not minHeap: # Nothing to worry about
                today = events[i][0]
            
            while i < n and events[i][0] == today: # For all the events that are hapening today
                heappush(minHeap, events[i][1])
                i += 1
            heappop(minHeap)
            res += 1
            today += 1
            while minHeap and minHeap[0] < today:
                heappop(minHeap)
        return res
        