class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        def calc(arr):
            res = 0
            for num in arr:
                res ^= num
            return res
        lst1 = [int(x) for x in list(bin(k)[2:])]
        a = [0] * (32 - len(lst1)) + lst1
        
        lst2 = [int(x) for x in list(bin(calc(nums))[2:])]
        b = [0] * (32 - len(lst2)) + lst2
        res = 0
        for i in range(len(a)):
            if a[i] != b[i]: res += 1
        return res
        