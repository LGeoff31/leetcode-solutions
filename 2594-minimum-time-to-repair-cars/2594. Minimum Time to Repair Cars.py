class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l, r = 0, 1e20
        res = 1e20
        def valid(minutes):
            c = 0
            for i in range(len(ranks)):
                c += floor(sqrt(minutes / ranks[i]))
            return c >= cars
        while l <= r:
            mid = (l + r) // 2
            print(mid, valid(mid))
            if valid(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return int(res)