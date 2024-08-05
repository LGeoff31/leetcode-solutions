class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        res = []
        for a,b,c,d,e in restaurants:
            if veganFriendly:
                if d <= maxPrice and e <= maxDistance and c == 1:
                    res.append((b,a))
            else:
                if d <= maxPrice and e <= maxDistance:
                    res.append((b,a))
        res.sort(reverse=True)
        a = []
        for p,b in res:
            a.append(b)
        return a

        