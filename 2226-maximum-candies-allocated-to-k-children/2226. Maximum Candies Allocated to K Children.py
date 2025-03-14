class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l, r = 0, max(candies)
        def valid(val):
            a = 0
            for i in range(len(candies)):
                if val != 0:
                    a += candies[i] // val
                else:
                    a += 1
            return a >= k
        while l <= r:
            mid = (l+r) // 2
            print('trying', mid, valid(mid))
            if valid(mid) or mid == 0:
                l = mid + 1
            else:
                r = mid - 1
        return max(r,0)