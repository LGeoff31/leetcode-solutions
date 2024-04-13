class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums = [-s for s in nums]
        heapq.heapify(nums)
        length = len(nums)
        for i in range(length): #0,1,2,3
            small = heapq.heappop(nums)
            # print(i, length - k)
            if i == (length - k):
                return small
            # print(nums)
        return -1