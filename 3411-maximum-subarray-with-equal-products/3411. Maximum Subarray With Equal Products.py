class Solution:
    def maxLength(self, nums: List[int]) -> int:

        def product(arr):
            res = 1
            for n in arr:
                res *= n
            return res
        
        def _lcm(arr):
            res = arr[0]
            for n in arr[1:]:
                res = lcm(res, n)
            return res
        
        def _gcd(arr):
            res = arr[0]
            for n in arr[1:]:
                res = gcd(res, n)
            return res
            
        res = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                subarr = nums[i: j+1]

                if product(subarr) == _lcm(subarr) * _gcd(subarr):
                    res = max(res, len(subarr))
        return res