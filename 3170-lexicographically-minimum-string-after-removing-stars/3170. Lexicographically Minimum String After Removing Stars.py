class Solution:
    def clearStars(self, s: str) -> str:
        minHeap = []
        for i,c in enumerate(s):
            if c == "*":
                heappop(minHeap)
            else:
                heappush(minHeap, (c, -i)) #it will pop up lowest character and index will be negative
        ans = [""]* len(s)
        while minHeap:
            ordChar, i = heappop(minHeap)
            ans[-i] = ordChar
        return "".join(ans)