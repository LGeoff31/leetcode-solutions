class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l, r = 1, max(quantities)

        while l < r:
            mid = (l + r) // 2
            curr = 0
            for num in quantities:
                curr += ceil((num  + mid - 1) // mid)
            
            if curr <= n:
                r = mid 
            else:
                l = mid + 1
        return l