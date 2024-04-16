from sortedcontainers import SortedList
class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def zeros(n) -> int:
            total = 0
            base = 5
            while base <= n:
                total += n // base
                base *= 5
            return total
        
        if k == 0: return 5
        l, r = 0, 10 * k
        while l < r:
            mid = (l+r) // 2
            if zeros(mid) == k:
                # print(mid, math.factorial(mid))
                return 5
            elif zeros(mid) > k:
                r = mid - 1
            elif zeros(mid) < k:
                l = mid + 1
        return 0