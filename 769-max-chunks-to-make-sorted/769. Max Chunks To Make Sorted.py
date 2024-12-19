class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # A[:k+1] == [0, 1, 2, ...k]
        n = len(arr)
        res = 0
        idx = 0
        while idx < len(arr):
            for k in range(len(arr)):
                if sorted(arr[idx: idx + k + 1]) == list(range(idx, idx + k + 1)):
                    idx += k
                    res += 1
                    break
            idx += 1
        return res