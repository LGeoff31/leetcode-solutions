class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        3,0,6,1,5

        [0,1,3,5,6]

        """
        citations.sort()
        res = -1e9
        n = len(citations)
        l, r = 0, len(citations)
        if l == r: return int(l != 0)
        def valid(num):
            return n - bisect_left(citations, num) >= num

        while l <= r:
            mid = (l + r) // 2
            print('mid', mid, valid(mid))
            if valid(mid):
                l = mid + 1
            else:
                r = mid - 1
         
        return r