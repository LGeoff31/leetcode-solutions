class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * (n+1)
        for start, end, val in bookings:
            res[start-1] += val
            res[end] -= val
        res = list(accumulate(res))
        return res[:-1]