from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n, r_queue, d_queue = len(senate), deque(), deque()
        for i in range(n):
            r_queue.append(i) if senate[i] == "R" else d_queue.append(i)

        while r_queue and d_queue:
            minNum = min(len(r_queue), len(d_queue))
            for i in range(minNum):
                r_queue.append(n) if r_queue[i] < d_queue[i] else d_queue.append(n)
                n += 1
            for i in range(minNum):
                r_queue.popleft()
                d_queue.popleft()
        return "Radiant" if r_queue else "Dire"
        