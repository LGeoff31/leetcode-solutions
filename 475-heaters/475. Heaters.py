class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        l, r = 0, 10**9
        heaters.sort()
        houses.sort()
        def valid(radius):
            idx = 0
            i = 0
            while i < len(heaters) and idx < len(houses):
                heaterPosition = heaters[i]
                minVal, maxVal = heaterPosition-radius, heaterPosition+radius
                if houses[idx] < minVal:
                    return False
                # Find the next position for idx
                idx = bisect_right(houses, maxVal)
                i += 1
                # print(idx, radius, maxVal)
            return idx == len(houses)
        while l <= r:
            mid = (l + r) // 2
            print(mid)
            if valid(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l