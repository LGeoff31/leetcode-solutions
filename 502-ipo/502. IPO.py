class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capitals: List[int]) -> int:
        minHeap = []
        n = len(profits)
        lst = [(c, p) for c,p in zip(capitals, profits)]
        lst.sort()
        visited = set()
        print(lst)
        i = 0
        for j in range(k): #O(K)
            while i < n and w >= lst[i][0]:
                if i not in visited:
                    visited.add(i) 
                    heapq.heappush(minHeap, -lst[i][1])
                i += 1
            #w should change
            if not len(minHeap):
                break
            w += -heapq.heappop(minHeap)

        return w