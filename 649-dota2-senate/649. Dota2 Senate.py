from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        r_queue = deque([])
        d_queue = deque([]) 
        for i in range(len(senate)):
            if senate[i] == "R":
                r_queue.append(i)
            else:
                d_queue.append(i)

        while r_queue and d_queue:
            minNum = min(len(r_queue), len(d_queue))
            for i in range(minNum):
                if r_queue[i] < d_queue[i]:
                    r_queue.append(n)
                else:
                    d_queue.append(n)
                n += 1
            for i in range(minNum):
                r_queue.popleft()
                d_queue.popleft()

        if r_queue: return "Radiant"
        else: return "Dire"
        