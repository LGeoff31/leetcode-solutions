class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        minHeap = []
        for a,b in classes:
            heappush(minHeap, (-((a+1)/(b+1) - a/b), a, b))
        for i in range(extraStudents):
            c,a,b = heappop(minHeap)
            heappush(minHeap, (-((a+2)/(b+2) - (a+1)/(b+1)), a+1, b+1))
        
        return sum(a/b for _, a,b in minHeap) / len(minHeap)


        """
        5/6 - 4/5 vs 4/6 - 3/5
        0.0333.   vs 0.0666

        3/6, 3/9, 4/5, 2/10

        5/6-4/5 vs 4/7 - 3/6

        3/4 - 2/3 vs 4/6 - 3/5
        """