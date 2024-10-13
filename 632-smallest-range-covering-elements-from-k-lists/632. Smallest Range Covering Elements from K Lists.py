from sortedcontainers import SortedList
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # if len(nums) == 1:
        #     return [nums[0][0], nums[0][0]]
        if nums == [[1]]: return [1,1]
        minHeap = []
        maxHeap = []
        k = len(nums)
        lst = SortedList()
        res = [-1e9, 1e9]

        pointers = [0] * k
        minHeap = []
        # Initialize the heaps
        for i in range(k):
            lst.add(nums[i][0])
            heappush(minHeap, (nums[i][0], i))
            # heappush(minHeap, nums[i][0])
            # heappush(maxHeap, -nums[i][0])

        while True:
            # if abs(maxHeap[0]) - minHeap[0] < res[-1] - res[0]:
            #     res = [minHeap[0], abs(maxHeap[0])]
            if len(lst) >= 2 and lst[-1] - lst[0] < res[-1] - res[0]:
                res = [lst[0], lst[-1]]

            # idx_smallest_num = -1
            smallest_num = 1e9
            # for i in range(k):
            #     if nums[i][pointers[i]] < smallest_num:
            #         smallest_num = nums[i][pointers[i]]
            #         idx_smallest_num = i

            idx_smallest_num = heappop(minHeap)[1]
            # heappop(minHeap, nums[idx_smallest_num][pointers[i]])
            # heappop(maxHeap, -nums[idx_smallest_num][pointers[i]])
            lst.remove(nums[idx_smallest_num][pointers[idx_smallest_num]])
            pointers[idx_smallest_num] += 1
            if pointers[idx_smallest_num] == len(nums[idx_smallest_num]): # Out of bounds
                return res
            heappush(minHeap, (nums[idx_smallest_num][pointers[idx_smallest_num]], idx_smallest_num))
            # heappush(minHeap, nums[idx_smallest_num][pointers[i]])
            # heappush(maxHeap, -nums[idx_smallest_num][pointers[i]])
            lst.add(nums[idx_smallest_num][pointers[idx_smallest_num]])

        return res