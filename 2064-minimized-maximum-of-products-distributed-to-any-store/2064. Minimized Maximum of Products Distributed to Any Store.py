class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l, r = 1, max(quantities)

        while l < r:
            mid = (l + r) // 2
            curr = 0
            print('trying', mid)
            for num in quantities:
                curr += ceil(num / mid)
            print(mid, curr)
            if curr <= n:
                r = mid 
            else:
                l = mid + 1
        return l