class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minHeap = [] # (freq, num) and maxLength should be k
        dic = Counter(nums)
        print(dic)
        for num, freq in dic.items():
            heappush(minHeap, ((freq, num)))
            if len(minHeap) > k:
                heappop(minHeap)
            print(minHeap)
        res = [num for _, num in minHeap]
        return res