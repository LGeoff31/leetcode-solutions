class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                subarr = arr[i:j+1]
                if len(subarr) % 2 == 1:
                    res += sum(subarr)
        return res