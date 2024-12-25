class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        dic = Counter(s)
        maxHeap = []
        for key in dic:
            heappush(maxHeap, (-dic[key], key))
        res = ""
        prevChar = "*"

        while maxHeap:
            occurences, character = heappop(maxHeap)
            if not maxHeap and character == prevChar: return ""
            if character == prevChar:
                realoccurences, realcharacter = heappop(maxHeap)
                heappush(maxHeap, (occurences, character))
                occurences, character = realoccurences, realcharacter
            occurences = -occurences
            res += character
            occurences -= 1
            if occurences != 0:
                heappush(maxHeap, (-occurences, character))
            prevChar = character
            print(res, maxHeap)

        return res