class Solution:
    def maximumLength(self, s: str) -> int:
        lst = [[1] * len(s) for _ in range(26)]
        dic = Counter(s)
        valid = False
        for key in dic:
            if dic[key] >= 3: valid = True
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                lst[ord(s[i]) - ord("a")][i] = 1 + lst[ord(s[i]) - ord("a")][i-1]
        def findThirdLargestELement(arr):
            q = []
            for num in arr:
                heapq.heappush(q, -num)
            # newArr = heapify(arr)
            heapq.heappop(q)
            heapq.heappop(q)
            return abs(heapq.heappop(q))

        res = -1
        for i in range(26):
            res = max(res, findThirdLargestELement(lst[i]))
        if valid: return max(res, 1)
        return -1

        
        