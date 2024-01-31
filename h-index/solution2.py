class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Time complexity O(nlogn)
        # Space complexity O(1)
        citations.sort()  # [0,1,3,5,6]
        max_count = 0
        for i in range(len(citations)):  # looking for 3 elements less than or eql
            if len(citations)-i <= citations[i]:
                max_count = max(max_count, len(citations)-i)
        return max_count
