class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        res = 0
        l, r = 0, max(position)
        position.sort()

        def force(val): #99999999
            idx = 0
            counter = 0

            while counter != m and idx < len(position):
                counter += 1
                idx = bisect.bisect_left(position, position[idx] + val)

            return counter == m

        while l <= r:
            mid = (l+r) // 2
            if force(mid):
                res = max(res, mid)
                l = mid + 1
            else:
                r = mid  -  1  
        return res



        