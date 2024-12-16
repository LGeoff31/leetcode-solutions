class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        # O(klogn)
        MOD = 10**9 + 7
        
        min_heap = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(min_heap)
        
        for _ in range(k):
            min_value, index = heapq.heappop(min_heap)
            new_value = (min_value * multiplier) % MOD
            
            heapq.heappush(min_heap, (new_value, index))
        
        result = [0] * len(nums)
        while min_heap:
            value, index = heapq.heappop(min_heap)
            result[index] = value
        
        return result
            