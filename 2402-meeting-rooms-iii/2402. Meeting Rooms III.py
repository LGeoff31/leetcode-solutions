class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        """
        If empty room, place lowest meeting id
        If no empty rooms, wait for room and put meeting with earliest start time
        Example 1
        1 | 1
        t=5s
        1 | 2
        t=10s
        2 | 2
        return meeting 0

        Simulation??
        SortedList / min heap + cnt array
        """
        meetings.sort()
        cnt = [0] * n
        q = SortedList() # (end_time, room)
        available_rooms = SortedList([i for i in range(n)])
        i = 0
        t = meetings[0][0]
        print(meetings)
        while i < len(meetings):
            if len(available_rooms) == 0:
                t = q[0][0]
                available_rooms.add(q[0][1])
                q.remove(q[0])
            if not q:
                t = meetings[i][0]
                q.add((meetings[i][1], 0))
                available_rooms.remove(0)
                cnt[0] += 1
                i+=1
                # print(q)
                # print(available_rooms)
                # print(cnt)
                # print()
                continue

            while q and q[0][0] <= meetings[i][0]:
                t = q[0][0]
                available_rooms.add(q[0][1])
                q.remove(q[0])

            smallest_available_room = available_rooms[0]
            if t > meetings[i][0]:
                # Delay
                duration = meetings[i][1] - meetings[i][0]
                q.add((t+duration, smallest_available_room))
                available_rooms.remove(smallest_available_room)
                cnt[smallest_available_room] += 1
            else:
                t = meetings[i][0]
                q.add((meetings[i][1], smallest_available_room))
                available_rooms.remove(smallest_available_room)
                cnt[smallest_available_room] += 1
            # print(q)
            # print(available_rooms)
            # print(cnt)
            # print()
            i += 1
            
        return cnt.index(max(cnt))
