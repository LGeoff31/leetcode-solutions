class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        # if sum(ribbons) < k: return 0

        l, r = 1, max(ribbons)
        res = 0
        while l <= r:
            mid = (l+r) // 2
            curr = 0
            for num in ribbons:
                curr += num // mid
            if curr >= k:
                res = max(res, mid)
                l = mid + 1
            else:
                r = mid - 1
        return res