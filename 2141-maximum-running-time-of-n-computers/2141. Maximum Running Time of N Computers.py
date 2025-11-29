class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        l, r = 0, 1e20

        def valid(val):
            return sum(min(b, val) for b in batteries) >= n * val

        res = -1e20
        while l <= r:
            mid = (l + r) // 2
            print('trying mid', mid, valid(mid))
            if valid(mid):
                res = max(res, mid)
                l = mid + 1
            else:
                r = mid - 1
        return int(res)