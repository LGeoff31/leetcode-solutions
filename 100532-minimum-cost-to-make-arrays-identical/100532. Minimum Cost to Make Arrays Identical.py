class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        res = 0
        for i in range(len(arr)):
            res += abs(arr[i] - brr[i])
        brr.sort()
        arr.sort()
        new_res = k
        for i in range(len(arr)):
            new_res += abs(arr[i] - brr[i])
        return min(res, new_res)