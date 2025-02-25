class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        curr = 0
        odd = 0
        for i in range(len(arr)):
            curr += arr[i]
            odd += curr % 2
        return odd + odd * (len(arr) - odd) % MOD 