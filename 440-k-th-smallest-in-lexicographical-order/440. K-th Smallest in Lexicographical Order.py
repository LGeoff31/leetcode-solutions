class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        curr = 1
        k -= 1
        def gap(a,b):
            res = 0
            while a <= n:
                res += min(n+1, b) - a
                a *= 10
                b *= 10
            return res
        while k > 0:
            step = gap(curr, curr+1)
            if step <= k:
                curr += 1
                k -= step
            else:
                curr *= 10
                k -= 1

        return curr