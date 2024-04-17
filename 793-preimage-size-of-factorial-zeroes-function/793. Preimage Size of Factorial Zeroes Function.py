from sortedcontainers import SortedList
class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def zeros(n) -> int:
            total = 0
            start = 5
            while start <= n: #34 -> 5: 6, 25: 1
                total += n // start
                start *= 5
            return total
        
        if k == 0: return 5
        l, r = 0, 6 * k
        while l < r:
            mid = (l+r) // 2
            if zeros(mid) == k:
                return 5
            elif zeros(mid) > k:
                r = mid - 1
            elif zeros(mid) < k:
                l = mid + 1
        return 0