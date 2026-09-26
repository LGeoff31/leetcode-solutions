class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        """
        Taking advantage of Lazy Deletion
        """
        res = []
        events = []
        max_heap = [0]
        deletion_heights = defaultdict(int)
        prev_height = 0

        for s, e, h in buildings:
            events.append((s, -h))
            events.append((e, h))

        events.sort()

        for x, height in events:
            if height < 0:
                heappush_max(max_heap, -height)
            else:
                deletion_heights[height] += 1
            
            while max_heap and max_heap[0] in deletion_heights:
                h = heappop_max(max_heap)
                deletion_heights[h] -= 1
                if deletion_heights[h] == 0:
                    del deletion_heights[h]
            
            if max_heap and max_heap[0] != prev_height:
                res.append([x, max_heap[0]])
                prev_height = max_heap[0]
        return res
