class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        minHeap = []
        for num in nums:
            heappush(minHeap, num)
        total = 0
        while len(minHeap) >= 2:
            a = heappop(minHeap)
            b = heappop(minHeap)
            if a >= k:
                return total
            heappush(minHeap, min(a,b)*2+max(a,b))
            total += 1
            # print(minHeap)
        return total
        