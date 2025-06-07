class Solution:
    def clearStars(self, s: str) -> str:
        minHeap = []
        lst = set()
        for i in range(len(s)):
            if s[i] == "*":
                val, idx = heappop(minHeap)
                lst.add(-idx)
            else:
                heappush(minHeap, (s[i],-i))
        res = ""
        idx = 0
        for i in range(len(s)):
            if i in lst or s[i] == "*":
                continue
            else:
                res += s[i]
        return res
            