class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capitals: List[int]) -> int:
        minHeap = []
        res = w
        lst = [(c, p) for c,p in zip(capitals, profits)]
        lst.sort() # Sort by capital
        idx = 0

        for i in range(k):
            while idx < len(lst) and w >= lst[idx][0]:
                heappush(minHeap, -lst[idx][1]) # If you have enough capital, add to minHeap the profit you'll gain
                idx += 1
            if len(minHeap) == 0: # Can't do anything more
                return res
            profit = -heappop(minHeap)
            res += profit
            w += profit
        return res