class Solution:
    def hIndex(self, citations: List[int]) -> int:
        minCitations = min(citations)
        maxCitations = max(citations)

        def numberAboveN(n):
            count = 0
            for num in citations:
                if n <= num:
                    count += 1
            return count

        for i in range(maxCitations, -1, -1):
            if numberAboveN(i) >= i:
                return i
        return -1
