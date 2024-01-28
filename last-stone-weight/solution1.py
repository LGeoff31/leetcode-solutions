class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        count = 0
        while len(stones) > 1:
            first_max = heapq.heappop(stones)
            secound_max = heapq.heappop(stones)
            if secound_max > first_max:
                heapq.heappush(stones, first_max - secound_max)
        return abs(stones[0]) if stones else 0
