class Solution:
    def minDifference(self, arr: List[int]) -> int:
        # Consider two min 1 max
        arr.sort()

        if len(arr) <= 4:
            return 0
        # Consider two max 1 min
        if len(arr) == 5:
            res = 1e9
            for i in range(1, len(arr)):
                res = min(res, arr[i] - arr[i-1])
            return res

        return min(arr[-1]-arr[3], arr[-4]-arr[0], arr[-3]-arr[1], arr[-2] - arr[2])

       #[0,1,1,4,6,6,6]