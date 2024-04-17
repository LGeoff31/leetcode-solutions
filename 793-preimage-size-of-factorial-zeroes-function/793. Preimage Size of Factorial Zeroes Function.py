class Solution:
    def preimageSizeFZF(self, k: int) -> int:   
        def zeros(n): #n=34 5: 6, 25: 1, 125: 
            start = 5
            res = 0
            while start <= n: 
                res += n // start
                start *= 5
            return res
        l, r = 0, 6*k
        while l<=r:
            mid = (l+r) // 2
            if zeros(mid) == k:
                return 5
            elif zeros(mid) > k:
                r = mid - 1
            else:
                l = mid + 1
        return 0
        



      