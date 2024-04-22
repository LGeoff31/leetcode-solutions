class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        res, acc, odd, even = 0, 0, 0, 0
        for i in range(len(arr)):
            acc += arr[i]
            if acc%2==1: 
                odd+=1
                res+=even+1
            else:
                even+=1
                res+=odd
        return res % MOD

