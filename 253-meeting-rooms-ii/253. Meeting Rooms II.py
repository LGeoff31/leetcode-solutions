class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        """
        Problem simplifies to, which vertical line generates the greatest intersection amongst the time intervals
        
        prefix = [0] * (10 ** 6 + 1)

        for start, end in intervals:
            prefix[start] += 1
            prefix[end] -= 1
        
        prefix = list(accumulate(prefix))
        return max(prefix)

        Time: O(n + end)
        space: O(end)
        
        """
        intervals.sort()
        max_room_allocation = 1
        s,e = intervals[0]
        min_heap = [e]

        print(intervals, min_heap)
        for start, end in intervals[1:]:
            while min_heap and min_heap[0] <= start:
                heappop(min_heap)

            heappush(min_heap, end)
            print(min_heap)
            max_room_allocation = max(max_room_allocation, len(min_heap))
    
        return max_room_allocation
