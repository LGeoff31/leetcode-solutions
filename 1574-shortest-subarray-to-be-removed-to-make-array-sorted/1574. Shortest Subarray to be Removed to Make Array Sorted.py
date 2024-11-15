class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        if len(arr) == 1: return 0
        n = len(arr)
        prefix = [arr[0]]
        for i in range(1, len(arr)):
            if arr[i] >= prefix[-1]:
                prefix.append(arr[i])
            else:
                break
        suffix = [arr[-1]]
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] <= suffix[-1]:
                suffix.append(arr[i])
            else:
                break
        if len(prefix) == n: return 0
        # if len(prefix) > 1 and len(prefix) == len(suffix): return len(prefix)
        suffix.sort()
        print(prefix, suffix)
        res = 1e9
        for i in range(len(prefix)):
            res = min(res, n - ((i+1) + len(suffix) - bisect_left(suffix, prefix[i])))
        for i in range(len(suffix) -1, -1, -1):
            res = min(res, n - ((len(suffix) - i) + bisect_right(prefix, suffix[i])))
        return res
