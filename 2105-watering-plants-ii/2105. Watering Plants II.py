class Solution:
    def minimumRefill(self, plants: List[int], c: int, d: int) -> int:
        n = len(plants)
        l, r = 0, n-1
        res = 0
        a,b = c,d
        while l <= r:
            if l == r:
                if max(a,b) >= plants[l]:
                    return res
                return res + 1

            if a >= plants[l]:
                a -= plants[l]
                l += 1
            else:
                res += 1
                a = c - plants[l]
                l += 1
            if b >= plants[r]:
                b -= plants[r]
                r -= 1
            else:
                res += 1
                b = d - plants[r]
                r -= 1
        return res

