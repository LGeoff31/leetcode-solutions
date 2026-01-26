class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        min_res = 1e9
        arr.sort()
        for i in range(1, len(arr)):
            min_res = min(min_res, arr[i] - arr[i-1])
        res = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == min_res:
                res.append((arr[i-1], arr[i]))
        return res