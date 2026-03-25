class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        """
        O(10^5) -> O(n) or O(nlogn)
        O(1000) -> O(n^2)
        O(10) -> O(2^n)
        """
        rows, cols = len(grid), len(grid[0])

        # Try all horizontal cuts
        prefix = [] # [6, 10, 12] -> row1 = 6, row2 = 4, row3 = 2
        for r in range(rows):
            cnt = 0
            for c in range(cols):
                cnt += grid[r][c]
            if not prefix:
                prefix.append(cnt)
            else:
                prefix.append(prefix[-1] + cnt)
        
        total_sum = prefix[-1]
        for r in range(rows):
            TOP_HALF = prefix[r]
            BOTTOM_HALF = total_sum - prefix[r]
            if TOP_HALF == BOTTOM_HALF:
                return True

        # Try all vertical cuts
        prefix = []
        for c in range(cols):
            cnt = 0
            for r in range(rows):
                cnt += grid[r][c]
            if not prefix:
                prefix.append(cnt)
            else:
                prefix.append(prefix[-1] + cnt)
        toatl_sum = prefix[-1]
        for c in range(cols):
            TOP_HALF = prefix[c]
            BOTTOM_HALF = total_sum - prefix[c]
            if TOP_HALF == BOTTOM_HALF:
                return True
        return False
