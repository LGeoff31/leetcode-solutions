class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        dic = defaultdict(int)
        minHeap = [] # (end_time, room)
        available_rooms = SortedList(range(0, n))
        # print(meetings)
        for i, (s, e) in enumerate(meetings):
            if not available_rooms:
                end_time, room = heappop(minHeap)
                available_rooms.add(room)
                if s >= end_time:
                    while minHeap and s >= minHeap[0][0]:
                        _, r = heappop(minHeap)
                        available_rooms.add(r)
                    heappush(minHeap, (e, available_rooms[0]))
                else:
                    heappush(minHeap, (end_time + (e-s), available_rooms[0]))
                dic[available_rooms[0]] += 1
                available_rooms.remove(available_rooms[0])
            else:
                while minHeap and s >= minHeap[0][0]:
                    _, r = heappop(minHeap)
                    available_rooms.add(r)

                dic[available_rooms[0]] += 1
                heappush(minHeap, (e, available_rooms[0]))
                available_rooms.remove(available_rooms[0])
            # print(available_rooms, minHeap, s, e)

        # a = list(sorted((value, key) for key, value in dic.items()))
        # print(a)
        lst = list(sorted((value, key) for key, value in dic.items()))
        max_value = max(a for a, _ in lst)
        for x,y in lst:
            if x == max_value:
                return y

        # return list(sorted((value, key) for key, value in dic.items()))[-1][1]