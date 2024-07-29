class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curr_avg = sum(arr[:k]) // k
        res= 1 if curr_avg >= threshold else 0
        for r in range(k, len(arr)):
            curr_avg = (curr_avg*k + arr[r] - arr[r-k]) / k
            if curr_avg >= threshold:
                res += 1
        return res
