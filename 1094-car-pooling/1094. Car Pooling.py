class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        lst = [0] * max(c for a,b,c in trips)
        for a, s, e in trips:
            lst[s] += a
            if e < len(lst):
                lst[e] -= a
        lst = list(accumulate(lst))
        return max(lst) <= capacity