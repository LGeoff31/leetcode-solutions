class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        #we want nums2 to be in descending order
        arr = []
        for a,b in zip(nums1, nums2):
            arr.append([b,a])
        arr.sort(reverse=True)
        a, b = [], [] #a denote the nums2
        for i in range(len(arr)):
            a.append(arr[i][0])
            b.append(arr[i][1])
        print(a)
        print(b)
        minHeap = []
        res = 0
        currSumHeap = 0
        for i in range(len(b)):
            currSumHeap += b[i]
            heapq.heappush(minHeap, b[i])
            if len(minHeap) == k + 1:
                currSumHeap -= heapq.heappop(minHeap)
            if len(minHeap) == k: res = max(res, currSumHeap * a[i])
            print("res", res)
        return res