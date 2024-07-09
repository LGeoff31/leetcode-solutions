class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        res = 0
        available = 0
        for a, b in customers:
            # If a >+ available: then the customer + b is the new available time and res increments by b
            # Else a < available: then the customer must wait available - a minutes, then process with b minutes, so available becomes available + b and res increments available - a + b
            if a >= available:
                available = a + b
                res += b
            else:
                res += available - a + b
                available = available + b
        return res / len(customers)
