class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        
        # stars and bars
        total_ways = ((n + 1) *(n + 2)) // 2

        overflow_1 = ((n - (limit + 1) + 1) * (n - (limit + 1) + 2)) // 2 if n >= (limit + 1) else 0

        overflow_2 = ((n - (2 * (limit + 1)) + 1) * (n - (2 * (limit + 1)) + 2)) // 2 if n >= 2 * (limit + 1) else 0

        overflow_3 = ((n - (3 * (limit + 1)) + 1) * (n - (3 * (limit + 1)) + 2)) // 2 if n >= 3 * (limit + 1) else 0

        return total_ways - 3 * overflow_1 + 3 * overflow_2 - overflow_3