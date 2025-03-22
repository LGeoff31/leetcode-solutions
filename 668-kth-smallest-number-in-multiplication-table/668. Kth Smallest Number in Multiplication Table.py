class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        l, r = 1, m*n
        def valid(mid):
            # Loop from row 1 to mid, add how many elements are <= mid from each of those rows using math, this should be O(R)
            count = 0
            for r in range(min(mid,m)):
                # r, 2*r, 3*r, ..., rc <= mid where c is maximized
                # c = mid / r
                count += min(mid // (r+1), n)
            return count >= k

        while l <= r:
            mid = (l + r) // 2
            print('mid', mid, valid(mid))
            if valid(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l