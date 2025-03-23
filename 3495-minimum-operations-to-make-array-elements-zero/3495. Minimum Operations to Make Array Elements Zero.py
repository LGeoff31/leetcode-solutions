class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        ans = 0
        for query in queries:
            start, end = query
            ops = 0
            prev = 1

            for d in range(1, 17):
                cur = prev * 4
                # Find the intersection between [start, end] and [prev, cur - 1]
                l = max(start, prev)
                r = min(end, cur - 1)
                if r >= l:
                    ops += (r - l + 1) * d
                prev = cur
            # Since each operation can reduce two division steps, we need ceil(ops / 2) operations.
            ans += (ops + 1) // 2
        return ans