class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        #[6, 8] 6
        #[0, 2] 2
        #[3, 5] 4

        # Idea, we want to maximimize the minimzation of differences between any two pair
        # Sort of evenly spread out each digit from the others

        # [2, 7] 2
        # [6, 11] 7
        # [13, 18] 13
        # [13, 18] 18 -> 16
        start.sort()

        def valid(diff):
            prev = start[0]
            for i in range(1, len(start)):
                min_val = max(prev + diff, start[i])
                if min_val > start[i] + d:
                    return False
                prev = min_val
            return True

        l, r = 0, start[-1] + d
        res = 0
        while l <= r:
            mid = l + (r-l) // 2
            if valid(mid):
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res

