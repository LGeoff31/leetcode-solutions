class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        res = [-1] * len(queries)
        minHeap = []

        # Preprocessing
        dic = defaultdict(list)
        for i, (a,b) in enumerate(queries):
            l, r = sorted(queries[i])
            if l == r or heights[r] > heights[l]:
                res[i] = r
            else:
                h = max(heights[r], heights[l])
                dic[r].append((h, i))
 
        for i in range(len(heights)):
            for group in dic[i]:
                heappush(minHeap, group)
            while minHeap and heights[i] > minHeap[0][0]:
                height, idx = heappop(minHeap)
                res[idx] = i
        return res

