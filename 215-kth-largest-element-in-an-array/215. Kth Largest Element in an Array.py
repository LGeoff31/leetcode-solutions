class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        length = len(nums)
        for i in range(length):
            smallestNum = heapq.heappop(nums)
            if i == (length - k): return smallestNum

